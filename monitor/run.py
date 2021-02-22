import os
from .dfWriterBase import *
from .dfWriterDaily import *
from .dfWriterInfo import *
from .historical.wallstreet import Stock, Call, Put
import yfinance as yf

#  run outside the root dir

stock_names = [
  "fb",
  "goog",
  "aapl",
  "baba",
  "amzn",
  "msft",
  "tsla",
  "nio",
  "nflx",
  "pins",
  "snap",
  "uber",
  "lyft",
  "xpev",
  "twtr",
  "pdd",
  "bili",
  "ba",
  "snow",
  "crm",
  "abnb",
]

etfs = [
  "qqq",
  "vti",
  "tqqq",
]

for stock_name in stock_names + etfs:
  dfb = dfWriterBase()
  path = os.getcwd() + "/chives/datahut/data/historical/" + stock_name + "/"
  s = Stock(stock_name)
  df = s.historical(days_back=40000, frequency="d")
  dfb.writeDfTo(path, df)

  dfb = dfWriterDaily()

  intervals = ["1m", "2m"]
  for interval in intervals:
    path = os.getcwd() + "/chives/datahut/data/daily/" \
                      + stock_name + "_" + interval + "/"
    period = "60d" if interval == "2m" else "7d"
    df = yf.download(stock_name, period=period, interval=interval, prepost=True)
    dfb.writeDfTo(path, df)
