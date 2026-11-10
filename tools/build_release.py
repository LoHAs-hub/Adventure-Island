"""Compatibility entry point for the current redo release; the rejected builder is in Git history."""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).with_name('build_redesign_release.py')), run_name='__main__')
