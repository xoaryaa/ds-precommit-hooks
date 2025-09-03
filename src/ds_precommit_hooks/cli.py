from typing import Optional
import typer
from .hooks import strip_notebook_outputs as s
from .hooks import large_file_blocker as l
from .hooks import simple_secret_scan as sec

app = typer.Typer(help="CLI for ds-precommit-hooks")

@app.command("strip-nb")
def strip_nb(path: str):
    s.main([path])

@app.command("block-large")
def block_large(path: str, max_bytes: int = typer.Option(25*1024*1024, "--max-bytes")):
    l.main(["--max-bytes", str(max_bytes), path])

@app.command("scan-secrets")
def scan_secrets(path: str):
    sec.main([path])

if __name__ == "__main__":
    app()
