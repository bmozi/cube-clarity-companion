"""Portable short-case demonstration for the computational chapter."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from cube_clarity.search import main
if __name__=='__main__':main()
