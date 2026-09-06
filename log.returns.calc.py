print('fuck forex')

import pandas as pd
import numpy as np

FILE_NAME = "BTCUSDT-1m-merged.csv"

df = pd.read_csv(
    FILE_NAME,
    usecols=["Close time", "Close"],
).rename(columns={
    "Close time": "close_time",
    "Close": "close"
})

df["close"] = pd.to_numeric(df["close"], errors="coerce")

df = df.dropna(subset=["close"]).reset_index(drop=True)
df["log_return"] = np.log(
    df["close"] / df["close"].shift(1)
)

calculations = df.loc[
    df["log_return"].notna(),
    ["close", "close_time", "log_return"],
].copy()

calculations["log_return_pct"] = calculations["log_return"] * 100

calculations.to_csv(
    "btc_log_returns.csv",
    index=False,
)

#wc -l btc_log_returns.csv
4701439 btc_log_returns.csv

wc -l BTCUSDT-1m-merged.csv
4701440 BTCUSDT-1m-merged.csv