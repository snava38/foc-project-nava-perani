import os
import sys

# Get the path of the 'conf' folder (where this file is located)
CONF_DIR = os.path.dirname(os.path.abspath(__file__))

# Path of the main 'project' folder
MAIN_DIR = os.path.abspath(os.path.join(CONF_DIR, '..'))

# Path of the 'notebooks' folder
NOTEBOOK_DIR = os.path.join(MAIN_DIR, 'notebooks')

# Path of the 'data' folder
DATA_DIR = os.path.join(MAIN_DIR, 'data')

# Add the path of the main folder to sys.path
sys.path.append(MAIN_DIR)
sys.path.append(DATA_DIR)

# Expose the paths to be imported in notebooks
__all__ = ['MAIN_DIR', 'NOTEBOOK_DIR', 'DATA_DIR']