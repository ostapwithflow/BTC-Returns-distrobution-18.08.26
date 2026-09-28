
#цей файл розраховує log returns та  фільтрує значення які не відповідають маштабу.


print('fuck forex')

import pandas as pd
import numpy as np

FILE_NAME = "BTCUSDT-1d-merged.csv"

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

is_five_minute = close_times.diff().between(
    pd.Timedelta(seconds=86399),
    pd.Timedelta(seconds=86401),
)

calculations = df.loc[
    df["log_return"].notna() & is_five_minute,
    ["close", "close_time", "log_return"]
].copy()

calculations["log_return_pct"] = calculations["log_return"] * 100

calculations.to_csv(
    "btc_log_returns.csv",
    index=False,
)
# Кількість рядків за wc -l, включно із заголовком:

#1m
# Обєднаний csv           4_701_440
# Дохідності до фільтра:   4_701_439
# Дохідності після:       4_701_389

#5m
# Обєднаний csv - 940298 
# Після фільтрації - 940248

#15m
# Обєднаний csv - 313439
# Після фільтрації - 313391

#30m 
# Обєднаний csv -  156726
# після фільтрації - 156680

#1h
# Обєднаний csv - 78,373
# після фільтрації - 78,329

#4h
# Обєднаний csv - 19,608
# після фільтрації - 19,570

#1d
# Обєднаний csv - 3,271
# 