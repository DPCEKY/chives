from wallstreet import Stock, Call, Put

names = ['AAPL', 'FB', 'GOOG', 'BABA', 'AMZN', 'MSFT', 'TSLA', 'NIO', 'NFLX', \
  'PINS', 'SNAP', 'UBER', 'LYFT', 'XPEV', 'TWTR', 'PDD']

for i in range(1000):
  name = names[(i + 1) % len(names)]
  print(name)
  s = Stock(name)
  print('stock = {}, price = {}, last_trade = {}'.format(name, s.price, s.last_trade))