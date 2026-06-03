#!/usr/bin/env python3
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent.parent
OUT_STATIC = ROOT / "output" / "static"
OUT_STATIC.mkdir(parents=True, exist_ok=True)

copied = 0
# copy top-level assets
for name in ("parsons.css", "parsons.js"):
    src = ROOT / name
    if src.exists():
        shutil.copy2(src, OUT_STATIC / src.name)
        copied += 1

# copy everything from lib/
libdir = ROOT / "lib"
if libdir.exists():
    for p in libdir.iterdir():
        if p.is_file():
            shutil.copy2(p, OUT_STATIC / p.name)
            copied += 1

# copy ui-extension assets (optional)
uidir = ROOT / "ui-extension"
if uidir.exists():
    for p in uidir.iterdir():
        if p.is_file():
            shutil.copy2(p, OUT_STATIC / p.name)
            copied += 1

print(f"Copied {copied} files into {OUT_STATIC}")
