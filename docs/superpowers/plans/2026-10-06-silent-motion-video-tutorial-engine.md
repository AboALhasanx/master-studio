# Silent Motion-Graphics Video Tutorial Engine Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a modular, automated video tutorial generator and produce a 30-minute, 100% silent motion-graphics master tutorial covering Advanced Software Engineering Chapter 4: Software Project Planning (Albrecht's FPA, UFP, VAF, 14 GSCs, and COCOMO).

**Architecture:** Decomposes the 30-minute curriculum into 9 independent, self-contained HTML/GSAP scenes ($2.5\text{--}4.0$ minutes each). A Python orchestrator (`video_builder.py`) validates each scene against HyperFrames gates (lint, layout, WCAG AA contrast), renders them locally in parallel via Headless Chromium, and executes an instant lossless FFmpeg stream concatenation into the final Master MP4.

**Tech Stack:** Python 3.12, Pytest, Node.js v24, `hyperframes@0.8.138`, GSAP 3.14.2, FFmpeg 9.0.2 (Gyan), Headless Chrome Shell.

**Spec:** `docs/superpowers/specs/2026-10-06-silent-motion-video-tutorial-engine-design.md`

## Global Constraints
- **Zero Human Voiceover:** The tutorial is 100% silent motion graphics. Teaching is conducted strictly via kinetic typography, animated boundary models, dynamic mathematical proofs, and bilingual subtitle strips.
- **Deterministic & Local (Zero-SaaS):** Rendered 100% locally on CPU/GPU via Headless Chrome Shell and FFmpeg 9.0.2. No third-party video APIs or paid subscriptions.
- **Quality Gates:** Every scene must pass `npx hyperframes check` with 0 errors, 0 runtime faults, and 100% WCAG AA contrast compliance prior to rendering.
- **Resolution & Codecs:** 1080p ($1920 \times 1080$), 30 fps, H.264 / AVC video stream.

---

### Task 1: Test-Driven Video Orchestrator (`video_builder.py`)

**Files:**
- Create: `90_Shared_Toolbox/tools/video_builder.py`
- Test: `tests/test_video_builder.py`

**Interfaces:**
- Produces:
  - `class VideoBuilder`:
    - `get_scene_hash(scene_dir: str) -> str`: Returns MD5 hash of `index.html` and assets.
    - `is_cache_valid(scene_dir: str, output_mp4: str) -> bool`: Verifies whether source hasn't changed since last render.
    - `generate_concat_manifest(scene_mp4s: list[str], manifest_path: str) -> str`: Writes valid FFmpeg concat text file.
    - `validate_scene(scene_dir: str) -> bool`: Runs `npx hyperframes check` and returns True if Exit Code 0.
    - `render_scene(scene_dir: str, output_mp4: str) -> bool`: Runs `npx hyperframes render` to emit scene MP4.
    - `stitch_master_video(manifest_path: str, master_output: str) -> bool`: Runs `ffmpeg -f concat -safe 0 -c copy`.

- [ ] **Step 1: Write the failing unit tests**

Create `tests/test_video_builder.py`:
```python
import os, tempfile, pytest
from pathlib import Path
from tools.video_builder import VideoBuilder

def test_generate_concat_manifest():
    builder = VideoBuilder()
    with tempfile.TemporaryDirectory() as tmpdir:
        parts = [
            os.path.join(tmpdir, "scene_01.mp4"),
            os.path.join(tmpdir, "scene_02.mp4")
        ]
        manifest_path = os.path.join(tmpdir, "concat.txt")
        builder.generate_concat_manifest(parts, manifest_path)
        
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
        os.utime(index_file, None)
        assert not builder.is_cache_valid(tmpdir, mp4_file)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_video_builder.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'tools.video_builder'`

- [ ] **Step 3: Implement `video_builder.py`**

Create `90_Shared_Toolbox/tools/video_builder.py`:
```python
"""
video_builder.py - Master Studio Silent Motion-Graphics Orchestrator
Validates, renders, and stitches modular HyperFrames scenes into master tutorials.
"""
import os, sys, glob, hashlib, subprocess
from pathlib import Path

class VideoBuilder:
    def __init__(self, ffmpeg_bin: str = "ffmpeg"):
        self.ffmpeg_bin = ffmpeg_bin

    def get_scene_hash(self, scene_dir: str) -> str:
        hasher = hashlib.md5()
        for root, _, files in sorted(os.walk(scene_dir)):
            for f in sorted(files):
                if f.endswith(('.html', '.css', '.js', '.json', '.svg', '.png')):
                    fp = os.path.join(root, f)
                    with open(fp, "rb") as fh:
                        hasher.update(fh.read())
        return hasher.hexdigest()

    def is_cache_valid(self, scene_dir: str, output_mp4: str) -> bool:
        if not os.path.exists(output_mp4):
            return False
        mp4_mtime = os.path.getmtime(output_mp4)
        for root, _, files in os.walk(scene_dir):
            for f in files:
                if f.endswith(('.html', '.css', '.js', '.json')):
                    fp = os.path.join(root, f)
                    if os.path.getmtime(fp) > mp4_mtime:
                        return False
        return True

    def generate_concat_manifest(self, scene_mp4s: list[str], manifest_path: str) -> str:
        lines = []
        manifest_dir = Path(manifest_path).parent
        for mp4 in scene_mp4s:
            # Use relative paths or forward-slashed paths for FFmpeg
            rel = Path(mp4).resolve().relative_to(manifest_dir.resolve()).as_posix()
            lines.append(f"file '{rel}'")
        Path(manifest_path).write_text("\n".join(lines) + "\n", encoding="utf-8")
        return manifest_path

    def validate_scene(self, scene_dir: str) -> bool:
        cmd = ["npx", "hyperframes", "check"]
        res = subprocess.run(cmd, cwd=scene_dir, capture_output=True, text=True, shell=True)
        return res.returncode == 0

    def render_scene(self, scene_dir: str, output_mp4: str, fps: int = 30) -> bool:
        abs_output = str(Path(output_mp4).resolve())
        cmd = [
            "npx", "hyperframes", "render",
            "--format=mp4",
            f"--fps={fps}",
            "-o", abs_output
        ]
        res = subprocess.run(cmd, cwd=scene_dir, capture_output=True, text=True, shell=True)
        return res.returncode == 0 and os.path.exists(output_mp4)

    def stitch_master_video(self, manifest_path: str, master_output: str) -> bool:
        cmd = [
            self.ffmpeg_bin, "-y",
            "-f", "concat",
            "-safe", "0",
            "-i", manifest_path,
            "-c", "copy",
            master_output
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        return res.returncode == 0 and os.path.exists(master_output)

if __name__ == "__main__":
    print("VideoBuilder CLI ready.")
```

- [ ] **Step 4: Run tests and verify they pass**

Run: `pytest tests/test_video_builder.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add 90_Shared_Toolbox/tools/video_builder.py tests/test_video_builder.py
git commit -m "feat(video): add test-driven VideoBuilder orchestrator tool"
```

---

### Task 2: Shared Silent Motion-Graphics Design System & Template

**Files:**
- Create: `01_Semester_1/04_Advanced_Software_Eng/05_Seminars_&_Slides/Ch04_Project_Planning_Video/common/theme.css`
- Create: `01_Semester_1/04_Advanced_Software_Eng/05_Seminars_&_Slides/Ch04_Project_Planning_Video/common/base_scene.html`

**Interfaces:**
- Consumes: HyperFrames landscape contract (`data-resolution="landscape"`, `1920x1080`).
- Produces: Reusable CSS styles for cards, chalkboards, boundary diagrams, metric counters, and bilingual caption bars.

- [ ] **Step 1: Write `theme.css`**

Create `common/theme.css` with dark slate palette, typography, WCAG AA contrast colors, and layout classes:
```css
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  width: 1920px;
  height: 1080px;
  overflow: hidden;
  background: #090d16;
  color: #f1f5f9;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}
#root {
  position: relative;
  width: 1920px;
  height: 1080px;
  background: radial-gradient(circle at 50% 20%, #151e33 0%, #090d16 85%);
  overflow: hidden;
}
.header-bar {
  position: absolute; top: 0; left: 0; width: 100%; height: 84px;
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 60px; background: rgba(15, 23, 42, 0.85);
  border-bottom: 1px solid rgba(56, 189, 248, 0.25);
  backdrop-filter: blur(12px); z-index: 100;
}
.brand-badge {
  background: #0369a1; color: #ffffff; font-size: 14px;
  font-weight: 800; padding: 6px 14px; border-radius: 6px;
  letter-spacing: 0.08em; text-transform: uppercase;
}
.course-name { font-size: 20px; font-weight: 700; color: #e2e8f0; }
.scene-pill {
  background: rgba(56, 189, 248, 0.12); border: 1px solid rgba(56, 189, 248, 0.35);
  color: #38bdf8; font-size: 15px; font-weight: 700; padding: 6px 18px; border-radius: 9999px;
}
.progress-line {
  position: absolute; top: 83px; left: 0; height: 3px; width: 0%;
  background: linear-gradient(90deg, #38bdf8, #818cf8, #34d399); z-index: 101;
}
.captions-bar {
  position: absolute; bottom: 0; left: 0; width: 100%; height: 110px;
  background: rgba(10, 15, 28, 0.96); border-top: 1px solid rgba(255, 255, 255, 0.12);
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  padding: 0 100px; text-align: center; gap: 6px; z-index: 100;
}
.caption-en { font-size: 22px; font-weight: 600; color: #f8fafc; }
.caption-ar { font-size: 18px; font-weight: 500; color: #7dd3fc; direction: rtl; }
```

- [ ] **Step 2: Commit**

```bash
git add 01_Semester_1/04_Advanced_Software_Eng/05_Seminars_&_Slides/Ch04_Project_Planning_Video/common/
git commit -m "feat(video): add common theme and layout styles for 30-min silent tutorial"
```

---

### Task 3: Author Scenes 01 & 02 (Foundations & FPA Origins)

**Files:**
- Create: `.../scenes/01_planning_and_loc/index.html` (180s)
- Create: `.../scenes/01_planning_and_loc/hyperframes.json`
- Create: `.../scenes/02_fpa_foundations/index.html` (180s)
- Create: `.../scenes/02_fpa_foundations/hyperframes.json`

**Interfaces:**
- Consumes: Aggarwal & Singh Chapter 4 (Slides 1–9), Conte's LOC definition.
- Produces: Renderable scenes 01 and 02 passing `npx hyperframes check`.

- [ ] **Step 1: Implement Scene 01 (180s)**
Build `scenes/01_planning_and_loc/index.html`:
- Planning triple constraints (Scope, Cost, Schedule).
- The LOC counting dilemma (18 lines vs 17 vs 13 executable statements).
- Conte's definition of Lines of Code.
- Timed GSAP animation across 180s with synchronized bilingual captions.

- [ ] **Step 2: Validate Scene 01**
Run: `cd .../scenes/01_planning_and_loc && npx hyperframes check`
Expected: `◇ Check passed` (0 errors, 0 warnings, 100% WCAG AA contrast).

- [ ] **Step 3: Implement Scene 02 (180s)**
Build `scenes/02_fpa_foundations/index.html`:
- 1979 Allan Albrecht (IBM) breakthrough.
- Sizing from requirements vs code.
- Language independence proof.
- Timed GSAP animation across 180s with synchronized bilingual captions.

- [ ] **Step 4: Validate Scene 02**
Run: `cd .../scenes/02_fpa_foundations && npx hyperframes check`
Expected: `◇ Check passed` (0 errors, 0 warnings).

- [ ] **Step 5: Commit**
```bash
git commit -m "feat(video): author scenes 01 and 02 for Ch04 planning tutorial"
```

---

### Task 4: Author Scenes 03 & 04 (Data Functions & Transactional Functions)

**Files:**
- Create: `.../scenes/03_data_functions_ilf_eif/index.html` (210s)
- Create: `.../scenes/04_tx_functions_ei_eo_eq/index.html` (210s)

**Interfaces:**
- Consumes: Aggarwal & Singh Chapter 4 (Slides 10–15).
- Produces: System boundary vector models, animated data packets, and transaction flows.

- [ ] **Step 1: Implement Scene 03 (210s)**
Build `scenes/03_data_functions_ilf_eif/index.html`:
- System boundary concept.
- Internal Logical Files (ILF): maintained within system.
- External Interface Files (EIF): maintained elsewhere, referenced here.
- Dynamic data packets animating into storage boxes.

- [ ] **Step 2: Validate Scene 03**
Run: `cd .../scenes/03_data_functions_ilf_eif && npx hyperframes check`
Expected: `◇ Check passed`.

- [ ] **Step 3: Implement Scene 04 (210s)**
Build `scenes/04_tx_functions_ei_eo_eq/index.html`:
- External Inputs (EI): incoming data mutating state.
- External Outputs (EO): outgoing derived reporting.
- External Inquiries (EQ): immediate read-only queries.
- Animated particle vectors crossing system boundaries.

- [ ] **Step 4: Validate Scene 04**
Run: `cd .../scenes/04_tx_functions_ei_eo_eq && npx hyperframes check`
Expected: `◇ Check passed`.

- [ ] **Step 5: Commit**
```bash
git commit -m "feat(video): author scenes 03 and 04 with animated boundary architecture"
```

---

### Task 5: Author Scenes 05 & 06 (Complexity Weights & Value Adjustment Factor)

**Files:**
- Create: `.../scenes/05_complexity_and_ufp/index.html` (210s)
- Create: `.../scenes/06_gsc_and_vaf/index.html` (210s)

**Interfaces:**
- Consumes: Weight matrices ($3..15$), 14 General System Characteristics ($F_1..F_{14}$).
- Produces: Kinetic math derivations and interactive metric counter animations.

- [ ] **Step 1: Implement Scene 05 (210s)**
Build `scenes/05_complexity_and_ufp/index.html`:
- Table of weights (Low, Average, High).
- Mathematical derivation of Unadjusted Function Points ($UFP = \sum W_{ij} Z_{ij}$).
- Animated counter accumulating sample points.

- [ ] **Step 2: Validate Scene 05**
Run: `cd .../scenes/05_complexity_and_ufp && npx hyperframes check`
Expected: `◇ Check passed`.

- [ ] **Step 3: Implement Scene 06 (210s)**
Build `scenes/06_gsc_and_vaf/index.html`:
- The 14 General System Characteristics (Data comms, performance, transaction rate, etc.).
- Degree of influence scale ($0$ to $5$).
- Technical Complexity Factor: $VAF = 0.65 + 0.01 \times \sum F_i$.

- [ ] **Step 4: Validate Scene 06**
Run: `cd .../scenes/06_gsc_and_vaf && npx hyperframes check`
Expected: `◇ Check passed`.

- [ ] **Step 5: Commit**
```bash
git commit -m "feat(video): author scenes 05 and 06 with UFP and VAF calculations"
```

---

### Task 6: Author Scenes 07, 08, 09 & Execute Master Render

**Files:**
- Create: `.../scenes/07_worked_numerical_exam/index.html` (240s)
- Create: `.../scenes/08_cocomo_and_putnam/index.html` (180s)
- Create: `.../scenes/09_exam_traps_summary/index.html` (150s)
- Output: `.../ASE_Ch04_Planning_Master_Tutorial.mp4` (~30 min continuous master)

**Interfaces:**
- Consumes: All 9 scenes, `video_builder.py`, local FFmpeg.
- Produces: 9 verified scene MP4s + final stitched 30-minute Master MP4 + snapshot frames.

- [ ] **Step 1: Implement Scenes 07, 08, and 09**
- Scene 07: Real exam problem step-by-step ($UFP$, $VAF$, and $FP = UFP \times VAF$).
- Scene 08: COCOMO modes (Organic, Semidetached, Embedded) + Putnam Rayleigh curve.
- Scene 09: Master review table & Dr. Ali Fahim exam traps.

- [ ] **Step 2: Validate all 3 scenes**
Run `npx hyperframes check` across scenes 07, 08, and 09.
Expected: `◇ Check passed` on all 3.

- [ ] **Step 3: Execute `video_builder.py` render & stitch**
Run:
```bash
python 90_Shared_Toolbox/tools/video_builder.py --render-all --stitch "01_Semester_1/04_Advanced_Software_Eng/05_Seminars_&_Slides/Ch04_Project_Planning_Video"
```
Expected: 
- 9 scene MP4s rendered into `rendered_parts/`.
- FFmpeg joins them into `ASE_Ch04_Planning_Master_Tutorial.mp4`.

- [ ] **Step 4: Verify with `ffprobe`**
Run:
```bash
ffprobe -v error -show_entries format=duration,size -of json "01_Semester_1/04_Advanced_Software_Eng/05_Seminars_&_Slides/Ch04_Project_Planning_Video/ASE_Ch04_Planning_Master_Tutorial.mp4"
```
Expected: Duration $\approx 1,800.0\text{ seconds}$ ($\pm 15\text{s}$), H.264, 1080p, 30 fps.

- [ ] **Step 5: Extract verification snapshots**
Extract 1 frame per scene to `snapshots/` and verify visual correctness.

- [ ] **Step 6: Commit and record in session journal**
```bash
git add ...
git commit -m "feat(video): deliver complete 30-min silent motion tutorial for Ch04 planning"
```
Append completion report to `00_STUDIO_HUB/sessions/2026-10-06.md`.
