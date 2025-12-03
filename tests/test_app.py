import os
import sys
from src.app import add

# Projekt-Root (Ordner "devops-ci-cd-training") zum Python-Pfad hinzufügen
CURRENT_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


def test_add():
    assert add(1, 2) == 3
