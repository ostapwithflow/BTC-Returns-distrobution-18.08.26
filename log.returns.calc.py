

print('fuck forex')

import pandas as pd
import numpy as np

FILE_NAME = "BTCUSDT-1m-merged.csv"

df = pd.read_csv(
    FILE_NAME,
    usecols=["Close time", "Close",]
).rename(columns={
    "Close time": "close_time",
    "Close": "close"
})


df["close"] = pd.to_numeric(df["close"], errors="coerce")
df = df.dropna(subset=["close"]).reset_index(drop=True)
df["log_return"] = np.log(
    df["close"] / df["close"].shift(1)
)

close_times = pd.to_datetime(
    df["close_time"],
    format="ISO8601",
    utc=True,
    errors="coerce",
)

is_one_minute = close_times.diff().between(
    pd.Timedelta(seconds=59),
    pd.Timedelta(seconds=61),
)

calculations = df.loc[
    df["log_return"].notna() & is_one_minute,
    ["close", "close_time", "log_return"]
].copy()

calculations["log_return_pct"] = calculations["log_return"] * 100

calculations.to_csv(
    "btc_log_returns.csv",
    index=False,
)

# Кількість рядків за wc -l, включно із заголовком:
# Вхідний CSV:             4_701_440
# Дохідності до фільтра:   4_701_439
# Дохідності після:       4_701_389
# Фільтр 59–61 с додатково відкинув 50 рядків.