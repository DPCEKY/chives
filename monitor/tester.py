import os
from .dfWriterBase import *
from .dfWriterDaily import *
from .dfWriterInfo import *
from .historical.wallstreet import Stock, Call, Put
import yfinance as yf

#  run outside the root dir

stock_names = [
  "fb",
  # "goog",
  # "aapl",
  # "baba",
  # "amzn",
  # "msft",
  # "tsla",
  # "nio",
  # "nflx",
  # "pins",
  # "snap",
  # "uber",
  # "lyft",
  # "xpev",
  # "twtr",
  # "pdd",
  # "bili",
  # "ba",
  # "snow",
  # "crm",
  # "abnb",
]

bond_names = [
  "qqq",
]

print(stock_names + bond_names)

for stock_name in stock_names:
  dfb = dfWriterInfo()
  path = os.getcwd() + "/chives/datahut/data/info/" + stock_name + "/"

  os.system('rm -rf ' + path)


  test_stock = yf.Ticker(stock_name)
  bs = test_stock.balance_sheet
  
  qbs = test_stock.quarterly_balance_sheet

  cf = test_stock.cashflow
  qcf = test_stock.quarterly_cashflow
  
  dfb.writeDfTo(path, bs, "bs")
  dfb.writeDfTo(path, qbs, "bs")
  dfb.writeDfTo(path, cf, "cf")
  dfb.writeDfTo(path, qcf, "cf")

  # dfb.readDfFrom(path)
