import sys, json

def _clean_cell(cell):
    if "outputs" in cell:
        cell["outputs"] = []
    if "execution_count" in cell:
        cell["execution_count"] = None
    return cell

def strip_notebook(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            nb = json.load(f)
        if "cells" in nb:
            nb["cells"] = [_clean_cell(c) for c in nb["cells"]]
        with open(path, "w", encoding="utf-8") as f:
            json.dump(nb, f, ensure_ascii=False, indent=1)
        return True
    except Exception as e:
        print(f"[strip-notebook-outputs] error processing {path}: {e}", file=sys.stderr)
        return False

def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if not argv:
        print("Usage: strip-notebook-outputs <notebook.ipynb>", file=sys.stderr)
        return 1
    ok = True
    for p in argv:
        if p.endswith(".ipynb"):
            ok = strip_notebook(p) and ok
    return 0 if ok else 1

if __name__ == "__main__":
    raise SystemExit(main())
