import os
from .dfWriterBase import *
from .dfWriterDaily import *
from .dfWriterInfo import *
from .portfolio_list import *
import yfinance as yf

#  run outside the root dir

for stock_name in high_tech + etfs + dow30:
  dfb = dfWriterBase()
  path = os.getcwd() + "/chives/datahut/data/historical/" + stock_name + "/"
  stock = yf.Ticker(stock_name)
  # get historical market data
  hist = stock.history(period="max")
  dfb.writeDfTo(path, hist)

  dfb = dfWriterDaily()

  intervals = ["1m", "2m"]
  for interval in intervals:
    path = os.getcwd() + "/chives/datahut/data/daily/" \
                      + stock_name + "_" + interval + "/"
    period = "60d" if interval == "2m" else "7d"
    df = yf.download(stock_name, period=period, interval=interval, prepost=True)
    dfb.writeDfTo(path, df)
