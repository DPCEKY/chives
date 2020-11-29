import argparse
import yfinance as yf

def parse_args():
	parser = argparse.ArgumentParser(description='Process stock info.')
	parser.add_argument('--stock_name', help='name of the stock')
	parser.add_argument('--period', help='time range of the stock, e.g. 1d, 5d')
	return parser.parse_args()

if __name__ == "__main__":
	args = parse_args()
	stock = yf.download(args.stock_name, period=args.period, interval="1m")
	print (stock)
