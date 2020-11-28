from dfWriterBase import *
from historical.wallstreet import Stock, Call, Put

dfb = dfWriterBase()
path='../datahut/data/historical/FB/'
s = Stock('FB')
df = s.historical(days_back=30000, frequency='d')

dfb.writeDfTo(path, df)