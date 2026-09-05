print("fuck forex")

import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt

import seaborn as sns
import seaborn.objects as so

FILE_NAME = "btc_log_returns.csv"
RETURN_COLUMN = "log_return_pct"

df = pd.read_csv(
    FILE_NAME,
    usecols=[RETURN_COLUMN])

X_MIN, X_MAX = -7.5, 7.5

fig, ax = plt.subplots(figsize=(14, 4))

sns.histplot(
    data=df,
    x=RETURN_COLUMN,
    bins=300,
    binrange=(X_MIN, X_MAX),
    ax=ax,
)

ax.set_xlim(X_MIN, X_MAX)

fig.tight_layout()
fig.savefig("btc_returns_distribution.png", dpi=300, bbox_inches="tight")


