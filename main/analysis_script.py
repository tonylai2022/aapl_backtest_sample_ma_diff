from facade.backtester import Backtester
import yfinance as yf

# get data
aapl_price_df = yf.download("AaPL", start="2018-01-01", end="2024-01-06", progress=False)

# data cleaning/data transformation
metric_price_df = aapl_price_df.dropna()
metric_price_df['signal'] = aapl_price_df['Close']
metric_price_df['price'] = aapl_price_df['Close']
signal_price_df = metric_price_df
signal_price_df = signal_price_df.dropna()

# backtest setup
backtester = Backtester(signal_price_df)
backtest_logic_name = 'momentum_ma_diff'
rolling_range = list(range(5, 50, 5))
pct_diff_thres_range = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1]
is_momentum = True
is_long_only = True
unit_tc = 0 # txn fee depends on the platform
annualized_factor = 252

# optimization
opt_df = backtester.create_optimization_df(backtest_logic_name, rolling_range, pct_diff_thres_range, unit_tc, is_momentum, is_long_only, annualized_factor)
result_df = backtester.extract_optimization_result_from_df()
opt_result_dict = backtester.backtest_momentum_ma_diff(25, 0.04, unit_tc, is_momentum, is_long_only, cache_df=True)
backtester.plot_equity_curve()

# data mining risk checking
backtester.plot_param_heatmap()




