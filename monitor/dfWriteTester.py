from dfWriterBase import *
from dfWriterDaily import *
from historical.wallstreet import Stock, Call, Put
import yfinance as yf

dfb = dfWriterBase()
path='../datahut/data/historical/goog/'
s = Stock('goog')
df = s.historical(days_back=40, frequency='d')
dfb.writeDfTo(path, df)

dfb = dfWriterDaily()
path='../datahut/data/daily/fb/'
df = yf.download('fb', period='5d', interval='1m')
dfb.writeDfTo(path, df)