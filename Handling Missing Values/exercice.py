# modules we'll use
import pandas as pd
import numpy as np

# read in all our data
sf_permits = pd.read_csv("/Users/mountasser/Desktop/Data Cleaning/NFL Play by Play 2009-2016 (v3).csv")

# set seed for reproducibility
np.random.seed(0) 

print(sf_permits.head())

