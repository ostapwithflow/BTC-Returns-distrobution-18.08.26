
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

