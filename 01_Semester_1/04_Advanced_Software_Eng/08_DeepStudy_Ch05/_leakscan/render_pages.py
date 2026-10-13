import sys, fitz, pathlib

pdf = pathlib.Path(sys.argv[1])
out = pathlib.Path(sys.argv[2])
zoom = float(sys.argv[3]) if len(sys.argv) > 3 else 1.6
pages = [int(x) for x in sys.argv[4].split(',')] if len(sys.argv) > 4 else None

out.mkdir(parents=True, exist_ok=True)
doc = fitz.open(pdf)
mat = fitz.Matrix(zoom, zoom)
sel = pages if pages else range(1, doc.page_count + 1)
for pn in sel:
    if pn < 1 or pn > doc.page_count:
        continue
    page = doc[pn - 1]
    pix = page.get_pixmap(matrix=mat)
    f = out / f"{pdf.stem}_p{pn:02d}.png"
    pix.save(str(f))
    print(f"{f.name}  {pix.width}x{pix.height}  imgs={len(page.get_images())}  chars={len(page.get_text().strip())}")
doc.close()
