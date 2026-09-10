import pandas as pd


FILENAME = "btc_log_returns.csv"
RETURNS_COLUMN = "log_return_pct"
DATE_COLUMN = "close_time"
YEAR = 2026

df = pd.read_csv(
    FILENAME,
    usecols=[DATE_COLUMN, RETURNS_COLUMN],
    parse_dates=[DATE_COLUMN],
)

df = df.set_index(DATE_COLUMN).sort_index()

x = df.loc[str(YEAR) , RETURNS_COLUMN]


LEVELS = [0.001, 0.01, 0.05, 0.25, 0.50, 0.75, 0.95, 0.99, 0.999]
q = x.quantile(LEVELS)

# MAD за визначенням: медіана абсолютних відхилень від медіани
mad = (x - x.median()).abs().median()

summary = pd.Series({
    "Count": x.count(),
    "Mean": x.mean(),
    "median": x.median(),
    "Std": x.std(),
    "MAD": mad,
    "IQR": q[0.75] - q[0.25],
    "std_vs_robust": x.std() / (1.4826 * mad),
    "skew": x.skew(),
    "excess_kurtosis": x.kurt(),
    "min": x.min(),
    "max": x.max(),
})

print(YEAR)
print(summary.to_string(float_format=lambda v: f"{v:.6f}"))
