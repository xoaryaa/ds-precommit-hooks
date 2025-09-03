import sys
import os

def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if not argv:
        print("Usage: large-file-blocker [--max-bytes N] <file...>", file=sys.stderr)
        return 1
    max_bytes = 25 * 1024 * 1024
    files = []
    i = 0
    while i < len(argv):
        if argv[i] == "--max-bytes":
            i += 1
            max_bytes = int(argv[i])
        else:
            files.append(argv[i])
        i += 1

    too_big = []
    for path in files:
        try:
            size = os.path.getsize(path)
            if size > max_bytes:
                too_big.append((path, size))
        except FileNotFoundError:
            # File might be deleted/renamed between staging and hook; ignore
            continue

    if too_big:
        print("[large-file-blocker] The following files exceed the limit:", file=sys.stderr)
        for p, s in too_big:
            print(f" - {p} ({s} bytes)", file=sys.stderr)
        print(f"Max allowed: {max_bytes} bytes. Adjust with --max-bytes.", file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
