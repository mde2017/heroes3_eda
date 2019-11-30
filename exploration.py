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

# print length of Unit_name column
print("Unit_name unique values:")
print(f"\t{len(list(data['Unit_name'].unique()))}")

# set Unit_name as index since column hat only distinct values
# data.set_index("Unit_name", inplace=True)

# filter columns by type
num_cols = [x for x in data.columns if data[x].dtype != "object"]
str_cols = [x for x in data.columns if data[x].dtype == "object"]


# analysis by castle
num_cols_castle = num_cols
num_cols_castle.append("Castle")
data_castle = data[reversed(num_cols_castle)]

# perfrom group by
data_castle_grouped = data_castle.groupby("Castle").sum()

# remove castle "neutral" since this castle not playable
data_castle_grouped.drop("Neutral", inplace=True)

data_castle_grouped.drop("AI_Value", axis=1, inplace=True)

# plot horizontal barcharts for each column
for idx, col in enumerate(data_castle_grouped.columns):
    # plot figure object
    fig = plt.figure(num=0)
    fig.set_size_inches(18.5, 10.5, forward=True)
    fig.tight_layout()
    ax = fig.add_subplot(2, 4, idx + 1)

    # sorted values
    asc = True
    if col == "Gold":
        asc = False

    sorted_col = data_castle_grouped[col].sort_values(ascending=asc)

    # create bar plot
    ax.barh(sorted_col.index, sorted_col.values, color="#26375e", zorder=2)

    # formatting
    ax.set_title(f"Feature: {col}")

    # remove spines
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_visible(False)

    # Draw vertical axis lines
    vals = ax.get_xticks()
    for tick in vals:
        ax.axvline(
            x=tick, linestyle="dashed", alpha=0.8, color="#eeeeee", zorder=1
        )

    # Set x-axis label
    ax.set_xlabel(f"{col}", labelpad=20, size=10)

    # Set y-axis label
    ax.set_ylabel("Castle", labelpad=20, size=10)

# save plot
fig.savefig(
    r"plots/stats_by_castle.png", dpi=100, bbox_inches="tight", pad_inches=0
)
