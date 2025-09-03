# Contributing

Thanks for helping! This project is designed to be contributor‑friendly and easy to review.

## Set up
```bash
git clone https://github.com/your-user/ds-precommit-hooks
cd ds-precommit-hooks
python -m venv .venv && source .venv/bin/activate  # on Windows: .venv\Scripts\activate
pip install -e ".[test]" -r requirements-dev.txt || pip install -e .
pip install pre-commit pytest ruff
pre-commit install
```

## Branching model
- `main` – stable branch (protected)
- `develop` – default branch for PRs
- `docs` – docs-only changes (optional)
- feature branches: `feat/<short-name>`; fixes: `fix/<short-name>`

## Making a change
1. Pick or open an issue. Small PRs are best.
2. Create a branch: `git checkout -b feat/add-new-hook`
3. Implement your hook under `src/ds_precommit_hooks/hooks/` and export it in `.pre-commit-hooks.yaml`
4. Add tests in `tests/`
5. Run `pre-commit run --all-files && pytest`
6. Open a PR to `develop` and fill the template.

## Good first issues to seed
- Add a new rule to `simple-secret-scan` (e.g., Slack tokens)
- Add `--allow-outputs` flag to `strip-notebook-outputs`
- Windows path edge-case for `large-file-blocker`
- Improve docs with animated GIFs
