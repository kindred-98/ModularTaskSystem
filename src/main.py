"""
main.py

Punto de entrada de la aplicación.
"""

import sys
import os

# Ajustar sys.path para que los imports internos funcionen
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ui.menu import menu

if __name__ == "__main__":
    menu()