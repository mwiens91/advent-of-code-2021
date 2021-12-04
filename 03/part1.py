#!/usr/bin/env python3

import pandas as pd

# Read file input
with open("input.txt") as f:
    lines = [x.rstrip() for x in f.readlines()]

# Convert each line into a list of strings
data = [list(line) for line in lines]

# Convert to dataframe
df = pd.DataFrame(data)

# Get most common digit
most_common = []

for i in range(len(df.columns)):
    most_common.append(df[i].value_counts().idxmax())

# Get the rates
gamma_rate = int("".join(most_common), 2)
epsilon_rate = int("".join(["1" if x == "0" else "0" for x in most_common]), 2)

# Print answer
print(gamma_rate * epsilon_rate)
