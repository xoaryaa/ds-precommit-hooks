import os
import tempfile
from ds_precommit_hooks.hooks.large_file_blocker import main as block_main

def test_large_file_blocker_allows_small_file():
    fd, path = tempfile.mkstemp()
    os.close(fd)
    with open(path, "wb") as f:
        f.write(b"hello")
    assert block_main([path]) == 0
