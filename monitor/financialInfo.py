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


dfb = dfWriterInfo()
for stock_name in stock_names:
  path = os.getcwd() + "/chives/datahut/data/info/" + stock_name + "/"

  company = yf.Ticker(stock_name)
  bs = company.balance_sheet
  qbs = company.quarterly_balance_sheet

  cf = company.cashflow
  qcf = company.quarterly_cashflow

  dfb.writeDfTo(path, bs, "bs")
  dfb.writeDfTo(path, qbs, "qbs")
  dfb.writeDfTo(path, cf, "cf")
  dfb.writeDfTo(path, qcf, "qcf")
