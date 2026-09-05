
# Цей скрипт обчислює логарифмічні доходності BTCUSDT з CSV файлу та зберігає результати у новий CSV файл.

print('fuck forex')

import numpy as np
import pandas as pd


# У CSV є рядок заголовків; читаємо лише потрібну колонку.
FILE_NAME = "BTCUSDT-1m-2017-08_to_2026-07.csv"


# Переведимо з міліскунд в мікросеку
df = pd.read_csv(
    FILE_NAME,
    usecols=["Open time", "Close time"],)

for col in ["Open time", "Close time"]:
    ts = df[col].astype("int64")

    # Приводимо ms та us до мікросекунд
    ts_us = ts.where(ts >= 10**14, ts * 1000)

    # Записуємо дату й час назад у ту саму колонку
    df[col] = pd.to_datetime(ts_us, unit="us", utc=True)


df.to_csv("BTCUSDT-1m-2017-08_to_2026-07.csv", index=False)


df = pd.read_csv(
    FILE_NAME,
    usecols=["Close"],
).rename(columns={"Close": "close"})


df["close"] = pd.to_numeric(df["close"], errors="coerce")

df = df.dropna(subset=["close"]).reset_index(drop=True)
df["log_return"] = np.log(
    df["close"] / df["close"].shift(1)
)

calculations = df.loc[
    df["log_return"].notna(),
    ["close", "log_return"],
].copy()

calculations["log_return_pct"] = calculations["log_return"] * 100

calculations.to_csv(
    "btc_log_returns.csv",
    index=False,
)

