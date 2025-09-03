# ds-precommit-hooks

Tiny, composable **pre-commit hooks for data/ML repos**:  
- 🧽 `strip-notebook-outputs` — remove outputs & execution counts from `.ipynb`  
- 🧱 `large-file-blocker` — prevent committing huge files (default >25MB)  
- 🔐 `simple-secret-scan` — flag likely secrets (basic regex + entropy)

> Perfect for teaching clean repo hygiene, and great for first-time OSS contributions.

## Quick start

```bash
pipx install pre-commit  # or: pip install pre-commit
pre-commit --version
```

Create `.pre-commit-config.yaml` in your project:

```yaml
repos:
  - repo: https://github.com/your-user/ds-precommit-hooks
    rev: v0.1.0
    hooks:
      - id: strip-notebook-outputs
      - id: large-file-blocker
        args: ["--max-bytes=26214400"]  # 25MB
      - id: simple-secret-scan
```

Then:

```bash
pre-commit install
git add .
git commit -m "chore: enable data-science pre-commit hooks"
```

## Hooks

### `strip-notebook-outputs`
- Clears cell outputs & execution counts to keep diffs readable.
- Only touches files passed by pre-commit.

### `large-file-blocker`
- Fails commit if any staged file exceeds a threshold (default 25MB).

### `simple-secret-scan`
- Flags common credential patterns (e.g., high-entropy strings, AWS-style keys).  
- Use alongside specialized scanners for stronger protection.

## CLI
A small CLI is included:

```bash
dsph strip-nb path/to/notebook.ipynb
dsph block-large --max-bytes 1048576 path/to/file.csv
dsph scan-secrets path/to/file.py
```

## Contributing

We love **first PRs**. Check out [`CONTRIBUTING.md`](CONTRIBUTING.md) and look for issues tagged
`good first issue` and `help wanted`. Add your own hook idea in `src/ds_precommit_hooks/hooks/`!

## License
MIT
