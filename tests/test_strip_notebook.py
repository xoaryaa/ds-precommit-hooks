import json
import os
import tempfile
from ds_precommit_hooks.hooks.strip_notebook_outputs import strip_notebook


def test_strip_notebook_outputs():
    nb = {"cells": [{"cell_type": "code", "execution_count": 5, "outputs": [{"text": "hi"}]}]}
    fd, path = tempfile.mkstemp(suffix=".ipynb")
    os.close(fd)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(nb, f)
    assert strip_notebook(path)
    with open(path, "r", encoding="utf-8") as f:
        out = json.load(f)
    assert out["cells"][0]["execution_count"] is None
    assert out["cells"][0]["outputs"] == []
