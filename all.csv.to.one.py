from pathlib import Path
import pandas as pd

folder =Path(__file__).resolve().parent/"csv"/"15m"

files = sorted(folder.glob("BTCUSDT-15m-????-??.csv"))

columns = [
    "Open time", "Open", "High", "Low", "Close", "Volume",
    "Close time", "Quote asset volume", "Number of trades",
    "Taker buy base asset volume", "Taker buy quote asset volume",
    "Ignore",
]

if not files:
    raise FileNotFoundError("Не знайдено місячних CSV для BTCUSDT")

output = folder / "BTCUSDT-15m-merged.csv"

with output.open("x", encoding="utf-8", newline="") as result:
    for i, file in enumerate(files):
        df = pd.read_csv(
            file,
            header=None,
            names=columns,
            dtype=str,
            keep_default_na=False,
        )

        df.to_csv(result, index=False, header=(i == 0))


