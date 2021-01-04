import pandas as pd
import os
from ..monitor.dfWriterBase import *
from ..monitor.dfWriterDaily import *
from ..monitor.historical.wallstreet import Stock, Call, Put


class dataLoader:
  def __init__(
    self,
    symbol="fb",
    load_path="chives/datahut/data/",
    mode="historical",
    interval="1m",
  ):
    self.data = {}
    self.symbol = symbol
    self.mode = mode
    self.interval = interval

    self.__load_data(load_path, mode, interval)

  def __load_data(self, load_path, mode, interval):
    if not mode in ["historical", "daily"]:
      print('[FETAL] invalid data mode! valid modes: "historical", "daily"')
      return

    load_path = os.path.abspath(load_path + "/" + mode)

    if mode == "historical":
      full_path = "{}/{}/".format(load_path, self.symbol)
    elif mode == "daily":
      full_path = "{}/{}_{}/".format(load_path, self.symbol, interval)

    print("[dataLoader] full_path = {}".format(full_path))

    if not os.path.exists(full_path):
      print("no {} data for {} in {}".format(mode, self.symbol, full_path))
      if mode == "historical":
        self.__download_historical_data(full_path, mode)

    self.__fetch_from_memory(full_path)

  def __fetch_from_memory(self, full_path):
    if self.mode == "historical":
      date_parser = pd.to_datetime

      for filename in os.listdir(full_path):
        file_path = os.path.join(full_path, filename)
        key = filename.split(".")[0]

        value = pd.read_csv(
          file_path, parse_dates=["Date"], date_parser=date_parser
        )
        value.set_index("Date", inplace=True)

        self.data[key] = value

    elif self.mode == "daily":
      print("mode {} data loading is not supported now".format(self.mode))
      pass

  def __download_historical_data(self, download_path, mode):
    dfb = dfWriterBase()
    s = Stock(self.symbol)
    # download all historical data here
    df = s.historical(days_back=36500, frequency="d")
    dfb.writeDfTo(download_path, df)

  def at(self, date="2012-05-21"):
    month = date
    if len(date) > len("2012-05"):
      month = "-".join(date.split("-")[:-1])

    month_data = self.data[month]

    row = month_data.loc[date]
    return row


if __name__ == "__main__":
  stock = dataLoader("goog")

  # data = loader.load_cfg()
  # print(data[0])
  # print("*" * 20)

  # print(data[1])
  # print("*" * 20)
  # print(data[2])

  # print("2020-10" > "2020-11")
  # print("2020-10" <= "2020-11")
  # print("2020-10-31" <= "2020-11")
  # print("2020-10" <= "2020-11-02")

  # print("2020-09-22" > "2020-01-23")
  # print("2020-09-22" <= "2020-01-23")

  row = stock.at("2020-01-23")
  print(type(row))
  print(row)
  print(row["Volume"])
