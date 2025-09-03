import tempfile
from ds_precommit_hooks.hooks.simple_secret_scan import main as scan_main


def test_secret_scan_flags_key():
    fd, path = tempfile.mkstemp(suffix=".txt")
    import os

    os.close(fd)
    with open(path, "w") as f:
        f.write("aws_secret_access_key = 'A' * 40")
    # Because our regex expects 40-base chars, this may not match; ensure test passes by using a realistic fake:
    with open(path, "w") as f:
        f.write("aws_secret_access_key = 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'")
    assert scan_main([path]) == 1
