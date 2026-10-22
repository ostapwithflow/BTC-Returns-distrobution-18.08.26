# Bitcoin Returns Distribution

An exploratory study of the statistical structure of BTC/USDT log returns across multiple timeframes. The aim is to look for patterns that persist across time scales and periods—not simply to compare calendar years or explain a particular year's returns.

## Research question

Do Bitcoin returns show recurring statistical properties across years and sampling intervals? The project calculates descriptive statistics and plots return distributions as a first step toward identifying such regularities. The results are descriptive: they do not establish a causal explanation or a universal law of Bitcoin markets.

## Data

The source is BTC/USDT candlestick (OHLCV) data from [Binance Vision](https://data.binance.vision/). The CSV schema contains open and close timestamps, OHLC prices, volume, trade count, and taker-buy volume fields.

The analysis covers these intervals:

- 1 minute
- 5 minutes
- 15 minutes
- 30 minutes
- 1 hour
- 4 hours
- 1 day

The project notes describe non-minute intervals as resampled from the native 1-minute series. The included scripts and archived return datasets are organized around these intervals, although several scripts currently have filenames and paths configured specifically for daily data.

Coverage is incomplete at the boundaries: 2017 starts on August 17, and 2026 ends on July 31 (inclusive). Therefore, those years are partial-year samples.

## Method

Returns are calculated close-to-close as logarithmic returns:

```text
log_return = ln(close[t] / close[t-1])
log_return_pct = log_return * 100
```

The processing notes describe the following workflow:

1. Combine monthly source CSV files into a single file.
2. Compare source and merged row counts as a basic integrity check.
3. Convert open and close timestamps to UTC.
4. Calculate log returns and filter intervals that do not match the selected timeframe.
5. Summarize and plot returns by calendar year.

Zero returns are retained. Removing them before resampling can leave too few observations to construct the higher-timeframe series consistently.

## Repository contents

| File or directory | Purpose |
| --- | --- |
| `all.csv.to.one.py` | Combines monthly CSV files from `csv/1d/` into a merged file. |
| `test.py` | Compares row counts of monthly source files and the merged CSV. |
| `To.utc_time.py` | Converts timestamps in a merged CSV to UTC. |
| `log.returns.calc.py` | Calculates close-to-close log returns and writes `btc_log_returns.csv`. |
| `stats.py` | Prints annual descriptive statistics for the configured returns CSV. |
| `visualize.py` | Creates annual histograms for the configured returns CSV. |
| `RAW.NUM.md` | Tables of annual summary statistics across the listed timeframes. |
| `Images/` | Annual return-distribution histograms by timeframe. |
| `archive/` | Archived return datasets, one ZIP per timeframe. |
| `Conclusion.md` | Working research notes and the motivation for the study. |
| `requirements.txt` | Pinned Python dependencies. |

## Statistics reported

`RAW.NUM.md` reports, by year and timeframe:

- observation count, mean, and median;
- standard deviation, median absolute deviation (MAD), and interquartile range (IQR);
- standard deviation relative to the scaled MAD (`std / (1.4826 × MAD)`);
- skewness, excess kurtosis, minimum, and maximum.

These measures help describe the center, spread, asymmetry, and tail behavior of the observed returns. They should be interpreted with the sampling interval and partial-year coverage in mind.

## Results and visualizations

The tables are in [`RAW.NUM.md`](RAW.NUM.md). Histograms are available under `Images/`, grouped by timeframe. For example:

![Daily BTC/USDT log-return distributions](Images/1d/histogram_2020.png)

The figures and statistics are exploratory evidence for further analysis. In particular, extreme observations and high kurtosis in some samples should not, by themselves, be treated as proof of a persistent distributional law or attributed to a single event.

## Setup

Python 3.14.4 was used for the pinned environment recorded in `requirements.txt`.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

## Running the scripts

The scripts expect their CSV inputs and outputs in the working directory or in the paths configured near the top of each file. For the merge and row-count scripts, monthly source files are expected under `csv/1d/` and named like `BTCUSDT-1d-YYYY-MM.csv`.

The return-calculation, statistics, and visualization scripts currently use fixed filenames and parameters in their source. Review and update those settings for the intended timeframe before running them. A typical daily-data sequence is:

```bash
python all.csv.to.one.py
python test.py
python To.utc_time.py
python log.returns.calc.py
python stats.py
python visualize.py
```

`visualize.py` saves histograms to its current working directory. The checked-in figures are stored separately under `Images/<timeframe>/`.

## Data availability

Raw and generated CSV files are excluded from Git by `.gitignore`. Source data must be obtained separately from Binance Vision. Archived return datasets are provided under `archive/` where included.

## Limitations

- 2017 and 2026 are partial years.
- The study describes historical samples and does not demonstrate causation or predict future returns.
- Return distributions may depend on timeframe, sampling, market regime, and data-cleaning choices.
- Some scripts are currently configured for daily files; paths and timeframe checks may need adjustment for other intervals.
- `requirements.txt` records the full captured environment, including transitive packages, rather than only direct dependencies.

## License

No license is currently specified. Add a `LICENSE` file before reuse or redistribution if you want to grant explicit permissions.
