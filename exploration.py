# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 18:40:33 2019

@author: micha
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# import raw data
data = pd.read_csv(r"data/H3Units.csv")

# print shape
print("Shape of data:")
print(f"\t{data.shape[0]} rows")
print(f"\t{data.shape[0]} columns")

# print column names & data type
print(f"Columns: ")
for i, col in enumerate(data.columns):
    print(f"\t{i}. {col} ({data[col].dtype})")
