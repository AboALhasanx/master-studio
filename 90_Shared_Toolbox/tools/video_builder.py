"""
video_builder.py - Master Studio Silent Motion-Graphics Orchestrator
Validates, renders, and stitches modular HyperFrames scenes into master tutorials.
"""
from __future__ import annotations

import argparse
import hashlib
import os
import subprocess
import sys
from pathlib import Path


class VideoBuilder:
    def __init__(self, ffmpeg_bin: str = "ffmpeg"):
        self.ffmpeg_bin = ffmpeg_bin

    def get_scene_hash(self, scene_dir: str) -> str:
        """Returns deterministic MD5 hash of scene HTML and asset files."""
        hasher = hashlib.md5()
        valid_extensions = (
            ".html", ".css", ".js", ".json", ".svg", ".png", ".jpg", ".jpeg", ".webp"
        )
        for root, _, files in sorted(os.walk(scene_dir)):
            for f in sorted(files):
                if f.lower().endswith(valid_extensions):
                    fp = os.path.join(root, f)
                    with open(fp, "rb") as fh:
                        hasher.update(fh.read())
        return hasher.hexdigest()

    def is_cache_valid(self, scene_dir: str, output_mp4: str) -> bool:
        """Verifies whether source files haven't changed since output_mp4 was built."""
        if not os.path.exists(output_mp4):
            return False
        mp4_mtime = os.path.getmtime(output_mp4)
        valid_extensions = (
            ".html", ".css", ".js", ".json", ".svg", ".png", ".jpg", ".jpeg", ".webp"
        )
        for root, _, files in os.walk(scene_dir):
            for f in files:
                if f.lower().endswith(valid_extensions):
                    fp = os.path.join(root, f)
                    if os.path.getmtime(fp) > mp4_mtime:
                        return False
        return True

    def generate_concat_manifest(self, scene_mp4s: list[str], manifest_path: str) -> str:
        """Writes an FFmpeg concat manifest file using forward-slashed paths."""
        lines = []
        manifest_dir = Path(manifest_path).parent.resolve()
        for mp4 in scene_mp4s:
            resolved_mp4 = Path(mp4).resolve()
            try:
                rel = resolved_mp4.relative_to(manifest_dir).as_posix()
            except ValueError:
                # If on different drives/roots, use absolute path formatted for ffmpeg
                rel = resolved_mp4.as_posix()
            lines.append(f"file '{rel}'")
        
        manifest_file = Path(manifest_path)
        manifest_file.parent.mkdir(parents=True, exist_ok=True)
        manifest_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return str(manifest_path)

    def validate_scene(self, scene_dir: str) -> bool:
        """Runs hyperframes check and returns True if Exit Code is 0."""
        hf_bin = "hyperframes.cmd" if sys.platform == "win32" else "hyperframes"
        cmd = [hf_bin, "check"]
        log_path = Path(scene_dir) / "check.log"
        log_path.parent.mkdir(parents=True, exist_ok=True)
        with open(log_path, "w", encoding="utf-8", errors="replace") as lf:
            res = subprocess.run(
                cmd,
                cwd=str(Path(scene_dir).resolve()),
                stdout=lf,
                stderr=subprocess.STDOUT,
                shell=sys.platform == "win32",
            )
        if res.returncode != 0:
            err_text = log_path.read_text(encoding="utf-8", errors="replace") if log_path.exists() else "No log"
            print(f"[!] Validation failed for {scene_dir}:\n{err_text}", file=sys.stderr)
        return res.returncode == 0

    def render_scene(self, scene_dir: str, output_mp4: str, fps: int = 30, retries: int = 3) -> bool:
        """Runs hyperframes render via safe staging path with retry support without pipe buffer deadlocks."""
        import shutil
        import tempfile
        import time

        abs_output = Path(output_mp4).resolve()
        abs_output.parent.mkdir(parents=True, exist_ok=True)

        staging_dir = Path(tempfile.gettempdir()) / "master_studio_renders"
        staging_dir.mkdir(parents=True, exist_ok=True)

        hf_bin = "hyperframes.cmd" if sys.platform == "win32" else "hyperframes"

        for attempt in range(1, retries + 1):
            temp_out = (staging_dir / f"{abs_output.stem}_{os.getpid()}_{attempt}.mp4").as_posix()
            log_file = staging_dir / f"{abs_output.stem}_{os.getpid()}_{attempt}.log"
            cmd = [
                hf_bin, "render",
                "--format=mp4",
                f"--fps={fps}",
                "-o", temp_out,
            ]
            if attempt > 1:
                print(f"[!] Retry {attempt}/{retries} rendering {Path(scene_dir).name}...")
                time.sleep(3)

            with open(log_file, "w", encoding="utf-8", errors="replace") as lf:
                res = subprocess.run(
                    cmd,
                    cwd=str(Path(scene_dir).resolve()),
                    stdout=lf,
                    stderr=subprocess.STDOUT,
                    shell=sys.platform == "win32",
                )
            if res.returncode == 0:
                if os.path.exists(temp_out):
                    shutil.move(temp_out, str(abs_output))
                    return True
                elif os.path.exists(str(abs_output)):
                    return True
                err_tail = log_file.read_text(encoding="utf-8", errors="replace")[-1000:] if log_file.exists() else "No log"
                print(f"[!] Attempt {attempt} failed for {Path(scene_dir).name}:\n{err_tail}", file=sys.stderr)
                if os.path.exists(temp_out):
                    try:
                        os.remove(temp_out)
                    except Exception:
                        pass

        return False
    def stitch_master_video(self, manifest_path: str, master_output: str) -> bool:
        """Runs ffmpeg concat demuxer to losslessly join all rendered scene parts."""
        abs_master = str(Path(master_output).resolve())
        os.makedirs(os.path.dirname(abs_master), exist_ok=True)
        cmd = [
            self.ffmpeg_bin, "-y",
            "-f", "concat",
            "-safe", "0",
            "-i", str(manifest_path),
            "-c", "copy",
            abs_master,
        ]
        res = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
        )
        return res.returncode == 0 and os.path.exists(master_output)

    def build_project(
        self,
        project_dir: str,
        output_name: str = "master_tutorial.mp4",
        fps: int = 30,
        force: bool = False,
    ) -> str:
        """Orchestrates validation, rendering, and stitching for a multi-scene project."""
        p_dir = Path(project_dir).resolve()
        scenes_dir = p_dir / "scenes"
        rendered_parts_dir = p_dir / "rendered_parts"
        rendered_parts_dir.mkdir(parents=True, exist_ok=True)

        scene_subdirs = sorted(
            [d for d in scenes_dir.iterdir() if d.is_dir() and (d / "index.html").exists()]
        )
        if not scene_subdirs:
            raise RuntimeError(f"No valid scenes found in {scenes_dir}")

        rendered_mp4s: list[str] = []
        for s_dir in scene_subdirs:
            scene_name = s_dir.name
            out_mp4 = rendered_parts_dir / f"{scene_name}.mp4"
            
            # Check validation
            print(f"[*] Validating scene: {scene_name}...")
            if not self.validate_scene(str(s_dir)):
                raise RuntimeError(f"Scene validation failed for {scene_name}")

            # Check cache
            if not force and self.is_cache_valid(str(s_dir), str(out_mp4)):
                print(f"[+] Scene {scene_name} is up to date (cached).")
            else:
                print(f"[>] Rendering scene {scene_name} @ {fps} fps...")
                success = self.render_scene(str(s_dir), str(out_mp4), fps=fps)
                if not success:
                    raise RuntimeError(f"Render failed for {scene_name}")

            rendered_mp4s.append(str(out_mp4))

        # Stitch
        manifest_file = rendered_parts_dir / "concat.txt"
        self.generate_concat_manifest(rendered_mp4s, str(manifest_file))
        
        master_output_path = p_dir / output_name
        print(f"[*] Stitching {len(rendered_mp4s)} scenes into {master_output_path.name}...")
        if not self.stitch_master_video(str(manifest_file), str(master_output_path)):
            raise RuntimeError(f"Stitching failed for {master_output_path}")

        print(f"[SUCCESS] Master video created at: {master_output_path}")
        return str(master_output_path)


def main():
    parser = argparse.ArgumentParser(description="Master Studio Video Builder CLI")
    parser.add_argument("project_dir", help="Directory containing scenes/ folder")
    parser.add_argument("-o", "--output", default="master_tutorial.mp4", help="Master output filename")
    parser.add_argument("--fps", type=int, default=30, help="Frames per second (default: 30)")
    parser.add_argument("--force", action="store_true", help="Force re-rendering of all scenes")
    args = parser.parse_args()

    builder = VideoBuilder()
    try:
        builder.build_project(args.project_dir, output_name=args.output, fps=args.fps, force=args.force)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
