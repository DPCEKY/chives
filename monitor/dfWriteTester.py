from dfWriterBase import *
from dfWriterDaily import *
from historical.wallstreet import Stock, Call, Put
import yfinance as yf

dfb = dfWriterBase()
stock_name = "fb"
path = "../datahut/data/historical/" + stock_name + "/"
s = Stock(stock_name)
df = s.historical(days_back=400, frequency="d")
dfb.writeDfTo(path, df)

dfb = dfWriterDaily()
interval="2m"
path = "../datahut/data/daily/" + stock_name + "_" + interval + "/"
df = yf.download(stock_name, period="60d", interval=interval, prepost=True)
dfb.writeDfTo(path, df)
