
# import libraries
import pandas as pd
import numpy as np
import math
import json
import matplotlib.pyplot as plt
import seaborn as sns

#%matplotlib inline

# read in the json files
portfolio = pd.read_json('I:/data_science/Starbucks/data/portfolio.json', orient='records', lines=True)
profile = pd.read_json('I:/data_science/Starbucks/data/data/profile.json', orient='records', lines=True)
transcript = pd.read_json('I:/data_science/Starbucks/data/data/transcript.json', orient='records', lines=True)

print(portfolio)