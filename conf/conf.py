import os
import sys

# Ottieni il percorso della cartella 'conf' (dove si trova questo file)
CONF_DIR = os.path.dirname(os.path.abspath(__file__))

# Percorso della cartella principale 'project'
MAIN_DIR = os.path.abspath(os.path.join(CONF_DIR, '..'))

# Percorso della cartella 'notebooks'
NOTEBOOK_DIR = os.path.join(MAIN_DIR, 'notebooks')

# Percorso della cartella 'data'
DATA_DIR = os.path.join(MAIN_DIR, 'data')

# Aggiungi il percorso della cartella principale a sys.path
sys.path.append(MAIN_DIR)
sys.path.append(DATA_DIR)

# Esporre i percorsi per essere importati nei notebook
__all__ = ['MAIN_DIR', 'NOTEBOOK_DIR', 'DATA_DIR']