import os
import pandas as pd

# Set the root directory path and path to data files
DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(DIR, 'data')

# Collect all the .txt files
files = [os.path.join(DATA_PATH, f)
         for f in os.listdir(DATA_PATH) if f.endswith('txt')]

# Get profile data

PROFILES = {}
for file in files:
    filename = file.split('\\')[-1].split('.txt')[0]
    if filename.startswith('FFA'):
        PROFILES[filename] = pd.read_csv(file, sep="\t", header=None)
    elif filename == 'cylinder':
        CYLINDER = pd.read_csv(file, sep='\t', header=None)
    elif filename == 'bladedat':
        BLADE = pd.read_csv(file, sep='\t', header=None)
        BLADE.columns = ['r', 'beta', 'c', 't/c']


""" 
Profiles stored as with keys:
FFA-W3-xxx

Display first five rows of the panda dataframe by:
PROFILES[profile-name].head()
"""
