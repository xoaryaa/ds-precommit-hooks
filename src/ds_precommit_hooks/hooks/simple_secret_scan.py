import sys
import re

# Very simple patterns; contributors can add more
PATTERNS = [
    re.compile(r"AKIA[0-9A-Z]{16}"),  # AWS Access Key ID
    re.compile(r"(?i)aws_secret_access_key\s*=\s*[\'\"][A-Za-z0-9/+=]{40}[\'\"]"),
    re.compile(r"(?i)api[_-]?key\s*[:=]\s*[\'\"][A-Za-z0-9_\-]{16,}[\'\"]"),
]


def is_text_file(path):
    try:
        with open(path, "rb") as f:
            chunk = f.read(1024)
        if b"\x00" in chunk:
            return False
        return True
    except Exception:
        return False


def scan_file(path):
    try:
        if not is_text_file(path):
            return []
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        findings = []
        for pat in PATTERNS:
            for m in pat.finditer(content):
                findings.append((path, m.group(0)[:6] + "…", m.start()))
        return findings
    except Exception:
        return []


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if not argv:
        print("Usage: simple-secret-scan <file...>", file=sys.stderr)
        return 1
    total = 0
    for path in argv:
        for p, snippet, pos in scan_file(path):
            print(
                f"[simple-secret-scan] potential secret in {p} at pos {pos}: {snippet}",
                file=sys.stderr,
            )
            total += 1
    if total > 0:
        print(
            "Refusing commit. If false positive, adjust patterns or add to allowlist.",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
