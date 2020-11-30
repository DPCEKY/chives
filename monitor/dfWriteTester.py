from dfWriterBase import *
from historical.wallstreet import Stock, Call, Put
import yfinance as yf

# dfb = dfWriterBase()
# path='../datahut/data/historical/fb/'
# s = Stock('fb')
# df = s.historical(days_back=30000, frequency='d')

dfb = dfWriterBase()
path='../datahut/data/daily/fb/'
df = yf.download('fb', period='1d', interval='1m')
dfb.writeDailyDfTo(path, df)