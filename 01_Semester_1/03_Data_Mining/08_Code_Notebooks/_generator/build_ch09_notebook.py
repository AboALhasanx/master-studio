# -*- coding: utf-8 -*-
"""
Builder for the Data Mining (CS602) Chapter 09 notebook.

Regenerates the .ipynb from the cell definitions in nb_cells.py and, with
--execute, runs every cell with nbclient so the delivered notebook carries live
outputs and embedded figures.

    python build_ch09_notebook.py             # build only
    python build_ch09_notebook.py --execute   # build + execute + save outputs

The notebook itself is the artefact a student reads; this script exists so the
notebook can be regenerated or patched deterministically after a review.
"""

import argparse
import importlib.util
import sys
from pathlib import Path

import nbformat as nbf

HERE = Path(__file__).resolve().parent
NOTEBOOK_DIR = HERE.parent
OUT_NAME = "Chapter09_Regression_in_Data_Mining.ipynb"


def load_cells():
    spec = importlib.util.spec_from_file_location("nb_cells", HERE / "nb_cells.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.CELLS


def build(out_path: Path):
    cells = load_cells()
    nb = nbf.v4.new_notebook()
    nb.cells = [
        nbf.v4.new_markdown_cell(src) if kind == "md" else nbf.v4.new_code_cell(src)
        for kind, src in cells
    ]
    nb.metadata.update({
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {
            "name": "python",
            "version": sys.version.split()[0],
            "mimetype": "text/x-python",
            "file_extension": ".py",
            "pygments_lexer": "ipython3",
            "nbconvert_exporter": "python",
            "codemirror_mode": {"name": "ipython", "version": 3},
        },
        "title": "Chapter 09 - Regression in Data Mining (Data Mining CS602)",
        "authors": [{"name": "Master Studio - Data Mining"}],
        "subject": "Regression in Data Mining: lecture formulas implemented, executed and explained",
        "keywords": ["data mining", "regression", "linear regression", "ridge", "lasso",
                     "elastic net", "decision tree", "random forest", "SVR", "metrics"],
    })
    nbf.write(nb, out_path)
    n_md = sum(1 for c in nb.cells if c.cell_type == "markdown")
    n_code = sum(1 for c in nb.cells if c.cell_type == "code")
    print(f"Wrote {out_path}\n  {len(nb.cells)} cells  ({n_md} markdown, {n_code} code)")
    return nb


def execute(nb, out_path: Path, cwd: Path):
    from nbclient import NotebookClient

    print(f"\nExecuting notebook (kernel cwd = {cwd}) ...")
    client = NotebookClient(
        nb,
        timeout=1800,
        kernel_name="python3",
        resources={"metadata": {"path": str(cwd)}},
        allow_errors=False,
    )
    client.execute()
    nbf.write(nb, out_path)
    print("Execution finished: no cell raised an error.")
    return nb


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--execute", action="store_true", help="execute the notebook and store outputs")
    ap.add_argument("--out", default=None, help="output .ipynb path")
    ap.add_argument("--cwd", default=None, help="working directory for execution")
    args = ap.parse_args()

    out_path = Path(args.out).resolve() if args.out else (NOTEBOOK_DIR / OUT_NAME)
    cwd = Path(args.cwd).resolve() if args.cwd else NOTEBOOK_DIR

    nb = build(out_path)
    if args.execute:
        execute(nb, out_path, cwd)


if __name__ == "__main__":
    main()
