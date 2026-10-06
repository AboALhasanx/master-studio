import os
import tempfile
import subprocess
from pathlib import Path
from unittest.mock import patch, MagicMock
import pytest

from tools.video_builder import VideoBuilder


def test_generate_concat_manifest():
    builder = VideoBuilder()
    with tempfile.TemporaryDirectory() as tmpdir:
        parts = [
            os.path.join(tmpdir, "scene_01.mp4"),
            os.path.join(tmpdir, "scene_02.mp4"),
        ]
        manifest_path = os.path.join(tmpdir, "concat.txt")
        result = builder.generate_concat_manifest(parts, manifest_path)

        assert result == manifest_path
        assert os.path.exists(manifest_path)
        content = Path(manifest_path).read_text(encoding="utf-8")
        assert "file 'scene_01.mp4'" in content
        assert "file 'scene_02.mp4'" in content


def test_cache_invalidation():
    builder = VideoBuilder()
    with tempfile.TemporaryDirectory() as tmpdir:
        index_file = os.path.join(tmpdir, "index.html")
        Path(index_file).write_text("<h1>Test</h1>", encoding="utf-8")
        mp4_file = os.path.join(tmpdir, "output.mp4")

        # When MP4 does not exist, cache is invalid
        assert not builder.is_cache_valid(tmpdir, mp4_file)

        # Create MP4
        Path(mp4_file).write_text("dummy mp4", encoding="utf-8")
        assert builder.is_cache_valid(tmpdir, mp4_file)

        # Modify index.html -> cache invalid
        Path(index_file).write_text("<h1>Modified</h1>", encoding="utf-8")
        # Touch index to ensure mtime is newer
        os.utime(index_file, (os.path.getmtime(mp4_file) + 10, os.path.getmtime(mp4_file) + 10))
        assert not builder.is_cache_valid(tmpdir, mp4_file)


def test_get_scene_hash():
    builder = VideoBuilder()
    with tempfile.TemporaryDirectory() as tmpdir:
        f1 = Path(tmpdir) / "index.html"
        f1.write_text("<div>Scene 1</div>", encoding="utf-8")
        hash1 = builder.get_scene_hash(tmpdir)
        assert isinstance(hash1, str)
        assert len(hash1) == 32

        # Changing content changes hash
        f1.write_text("<div>Scene 1 modified</div>", encoding="utf-8")
        hash2 = builder.get_scene_hash(tmpdir)
        assert hash1 != hash2


def test_validate_scene_mocked():
    builder = VideoBuilder()
    with patch("subprocess.run") as mock_run:
        mock_run.return_value = MagicMock(returncode=0)
        assert builder.validate_scene("dummy_dir") is True
        mock_run.assert_called_once()

        mock_run.return_value = MagicMock(returncode=1)
        assert builder.validate_scene("dummy_dir") is False


def test_render_scene_mocked():
    builder = VideoBuilder()
    with tempfile.TemporaryDirectory() as tmpdir:
        output_mp4 = os.path.join(tmpdir, "out.mp4")
        with patch("subprocess.run") as mock_run:
            def side_effect(*args, **kwargs):
                Path(output_mp4).write_text("video-data", encoding="utf-8")
                return MagicMock(returncode=0)
            mock_run.side_effect = side_effect

            assert builder.render_scene(tmpdir, output_mp4) is True
            assert os.path.exists(output_mp4)


def test_stitch_master_video_mocked():
    builder = VideoBuilder(ffmpeg_bin="ffmpeg")
    with tempfile.TemporaryDirectory() as tmpdir:
        manifest = os.path.join(tmpdir, "manifest.txt")
        master = os.path.join(tmpdir, "master.mp4")
        Path(manifest).write_text("file 'dummy.mp4'", encoding="utf-8")

        with patch("subprocess.run") as mock_run:
            def side_effect(*args, **kwargs):
                Path(master).write_text("stitched-data", encoding="utf-8")
                return MagicMock(returncode=0)
            mock_run.side_effect = side_effect

            assert builder.stitch_master_video(manifest, master) is True
            assert os.path.exists(master)


def test_build_project_end_to_end_mocked():
    builder = VideoBuilder()
    with tempfile.TemporaryDirectory() as tmpdir:
        project_dir = Path(tmpdir)
        scenes_dir = project_dir / "scenes"
        scene_1 = scenes_dir / "01_intro"
        scene_2 = scenes_dir / "02_core"
        scene_1.mkdir(parents=True)
        scene_2.mkdir(parents=True)
        (scene_1 / "index.html").write_text("<h1>Scene 1</h1>", encoding="utf-8")
        (scene_2 / "index.html").write_text("<h1>Scene 2</h1>", encoding="utf-8")

        with patch.object(builder, "validate_scene", return_value=True) as mock_val, \
             patch.object(builder, "render_scene", return_value=True) as mock_render, \
             patch.object(builder, "stitch_master_video", return_value=True) as mock_stitch:

            # Create mock mp4s when rendered
            def fake_render(s_dir, out_mp4, fps=30):
                Path(out_mp4).write_text("fake mp4", encoding="utf-8")
                return True

            mock_render.side_effect = fake_render

            def fake_stitch(manifest, out_master):
                Path(out_master).write_text("master mp4", encoding="utf-8")
                return True

            mock_stitch.side_effect = fake_stitch

            master_path = builder.build_project(str(project_dir), output_name="out.mp4")
            assert os.path.exists(master_path)
            assert mock_val.call_count == 2
            assert mock_render.call_count == 2
            assert mock_stitch.call_count == 1


def test_build_project_validation_failure():
    builder = VideoBuilder()
    with tempfile.TemporaryDirectory() as tmpdir:
        project_dir = Path(tmpdir)
        scene_1 = project_dir / "scenes" / "01_intro"
        scene_1.mkdir(parents=True)
        (scene_1 / "index.html").write_text("<h1>Scene 1</h1>", encoding="utf-8")

        with patch.object(builder, "validate_scene", return_value=False):
            with pytest.raises(RuntimeError, match="validation failed"):
                builder.build_project(str(project_dir))
