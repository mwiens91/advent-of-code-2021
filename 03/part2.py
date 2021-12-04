#!/usr/bin/env python3

import pandas as pd

# Read file input
with open("input.txt") as f:
    lines = [x.rstrip() for x in f.readlines()]

# Convert each line into a list of strings
data = [list(line) for line in lines]

# Convert to dataframe
df = pd.DataFrame(data)

# Find oxygen generator rating
valid_rows = pd.Series([True for _ in range(len(df.index))])

for i in range(len(df.columns)):
    counts = df[valid_rows][i].value_counts()

    try:
        if counts.iloc[0] == counts.iloc[1]:
            val = '1'
        else:
            val = counts.idxmax()
    except IndexError:
        val = counts.idxmax()

    valid_rows_here = df[i] == val
    valid_rows = valid_rows & valid_rows_here

oxygen_rating = int("".join(df.loc[valid_rows].values.flatten().tolist()), 2)

# Find CO2 generator rating
valid_rows = pd.Series([True for _ in range(len(df.index))])

for i in range(len(df.columns)):
    counts = df[valid_rows][i].value_counts(ascending=True)

    try:
        if counts.iloc[0] == counts.iloc[1]:
            val = '0'
        else:
            val = counts.idxmin()
    except IndexError:
        val = counts.idxmin()

    valid_rows_here = df[i] == val
    valid_rows = valid_rows & valid_rows_here

co2_rating = int("".join(df.loc[valid_rows].values.flatten().tolist()), 2)

# Print answer
print(oxygen_rating * co2_rating)
