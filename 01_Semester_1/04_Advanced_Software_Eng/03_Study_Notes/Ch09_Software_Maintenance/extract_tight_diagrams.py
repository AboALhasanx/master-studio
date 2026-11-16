import fitz
import os
from PIL import Image

pdf_path = r"01_Semester_1\04_Advanced_Software_Eng\02_Raw_Materials\Aggarwal_Singh_SE_3rd_ed_By_Chapter\Ch09_Software_Maintenance.pdf"
out_dir = r"01_Semester_1\04_Advanced_Software_Eng\03_Study_Notes\Ch09_Software_Maintenance\diagrams"
os.makedirs(out_dir, exist_ok=True)

doc = fitz.open(pdf_path)

# Precise clip rectangles for each figure (x0, y0, x1, y1) in slide 792x612 pt coordinates
# Header is above y=110, footer is below y=555.
# Captions: "Fig. X" can be excluded or kept cleanly at bottom.
clips = {
    # Fig 2: Maintenance process (raster image xref 50 at [216, 144, 532, 540])
    "CH09_FIG02_Maintenance_Process.png": (9, fitz.Rect(214, 140, 534, 535)),
    
    # Fig 3: Quick fix model
    "CH09_FIG03_Quick_Fix_Model.png": (12, fitz.Rect(200, 150, 600, 520)),
    
    # Fig 4: Iterative enhancement model
    "CH09_FIG04_Iterative_Enhancement.png": (14, fitz.Rect(140, 140, 660, 490)),
    
    # Fig 5: Reuse model
    "CH09_FIG05_Reuse_Model.png": (16, fitz.Rect(200, 150, 600, 495)),
    
    # Fig 6: Boehm model
    "CH09_FIG06_Boehms_Model.png": (18, fitz.Rect(120, 140, 680, 480)),
    
    # Fig 7: Taute maintenance model (tight crop excluding text at y<208)
    "CH09_FIG07_Taute_Model.png": (19, fitz.Rect(212, 210, 584, 538)),
    
    # Fig 10: Mapping between application and program domains
    "CH09_FIG10_Domain_Mapping.png": (41, fitz.Rect(180, 155, 620, 520)),
    
    # Fig 11: Levels of abstraction (raster image xref 146 at [114, 162, 668, 449])
    "CH09_FIG11_Reverse_Eng_Levels.png": (44, fitz.Rect(112, 160, 670, 452)),
    
    # Fig 12: Comparison of new software development with re-engineering
    "CH09_FIG12_New_Dev_vs_Reeng.png": (47, fitz.Rect(90, 150, 710, 510)),
    
    # Fig 13: Restructuring a program (raster image xref 162 at [84.6, 188.6, 708.2, 424.2])
    "CH09_FIG13_Program_Restructuring.png": (51, fitz.Rect(84, 188, 709, 425)),
    
    # Fig 14: Change request form (raster image xref 176 at [192, 115, 606, 512])
    "CH09_FIG14_Change_Request_Form.png": (57, fitz.Rect(190, 115, 608, 514)),
}

for filename, (slide_idx, clip_rect) in clips.items():
    page = doc[slide_idx]
    # Render at 300 DPI (scale = 300 / 72 = 4.1667)
    zoom = 300.0 / 72.0
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat, clip=clip_rect, alpha=False)
    
    out_path = os.path.join(out_dir, filename)
    pix.save(out_path)
    
    # Autocrop white borders using PIL
    im = Image.open(out_path)
    # Convert to grayscale to find bounding box of non-white content
    gray = im.convert("L")
    # threshold 250
    bw = gray.point(lambda x: 0 if x < 250 else 255, '1')
    bbox = bw.getbbox()
    if bbox:
        # add 8px padding
        pad = 8
        w, h = im.size
        box = (max(0, bbox[0]-pad), max(0, bbox[1]-pad), min(w, bbox[2]+pad), min(h, bbox[3]+pad))
        cropped = im.crop(box)
        cropped.save(out_path)
        print(f"[+] Saved tight crop {filename}: {cropped.size[0]}x{cropped.size[1]}px")
    else:
        print(f"[+] Saved {filename}: {im.size[0]}x{im.size[1]}px")

print("All 11 diagrams extracted and cropped tightly.")
