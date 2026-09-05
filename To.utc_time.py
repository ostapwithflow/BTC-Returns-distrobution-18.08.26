
# Цей скрипт обчислює логарифмічні доходності BTCUSDT з CSV файлу та зберігає результати у новий CSV файл.

import pandas as pd

FILE_NAME = "BTCUSDT-1m-merged.csv"

# Читаємо всі колонки як текст, щоб зберегти інші значення.
df = pd.read_csv(FILE_NAME, dtype=str, keep_default_na=False)

for col in ["Open time", "Close time"]:
    values = df[col].str.strip()
    numbers = pd.to_numeric(values, errors="coerce")
    is_number = numbers.notna()

    result = pd.Series(
        pd.NaT,
        index=df.index,
        dtype="datetime64[ns, UTC]",
    )

    # Числові timestamp: розрізняємо ms та us.
    ts = numbers.loc[is_number].astype("int64")
    ts_us = ts.where(ts >= 10**14, ts * 1000)

    result.loc[is_number] = pd.to_datetime(
        ts_us, unit="us", utc=True
    )

    # Уже записані дати: з дробовими секундами або без.
    result.loc[~is_number] = pd.to_datetime(
        values.loc[~is_number],
        format="mixed",
        utc=True,
    )

    df[col] = result.dt.floor("s")

df.to_csv(FILE_NAME, index=False)