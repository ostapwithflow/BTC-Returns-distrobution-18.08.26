
print("fuck forex")

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn.objects as so


FILENAME = "btc_log_returns.csv"
DATE_COLUMN = "close_time"
RETURNS_COLUMN = "log_return_pct"

YEAR = [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]

df = pd.read_csv(
    FILENAME,
    usecols=[DATE_COLUMN, RETURNS_COLUMN],
    parse_dates=[DATE_COLUMN],
).set_index(DATE_COLUMN).sort_index()

for year in YEAR:
    x = df.loc[str(year), RETURNS_COLUMN].dropna()

    plt.figure()
    sns.histplot(x, bins=200)
    plt.title(f"{year}")
    plt.xlabel("%")
    plt.gca().spines["bottom"].set_visible(False) 
    plt.savefig(f"histogram_{year}.png", dpi=300, bbox_inches="tight")  
    plt.close()