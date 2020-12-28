import json
import os
import pandas as pd


class packed_bt_data:
  def __init__(self):
    self.data = {}


class expt_loader:
  def __init__(self):
    self.expt_cfg = {}
    self.control_cfg = {}
    self.test_cfg = {}

  def load_cfg(
    self, oe_name="example_expt_0", expt="expt", control="control", test="test"
  ):
    oe_path = os.getcwd() + "/oe_test/" + oe_name + "/"

    if not os.path.exists(oe_path):
      print("empty {} input! return..".format(oe_path))
      return

    # Opening JSON file
    expt_cfg_ptr = open(oe_path + expt + ".json")
    control_cfg_ptr = open(oe_path + control + ".json")
    test_cfg_ptr = open(oe_path + test + ".json")

    # returns JSON object as a dictionary
    self.expt_cfg = json.load(expt_cfg_ptr)
    self.control_cfg = json.load(control_cfg_ptr)
    self.test_cfg = json.load(test_cfg_ptr)

    # Closing file
    expt_cfg_ptr.close()
    control_cfg_ptr.close()
    test_cfg_ptr.close()

    return self.expt_cfg, self.control_cfg, self.test_cfg

  def load_data(
    self, oe_name="example_expt_0", expt="expt", control="control", test="test"
  ):
    if len(self.expt_cfg) == 0:
      self.load_cfg(oe_name, expt, control, test)

    stocks = self.expt_cfg["stocks"]
    symbols = []
    for stock in stocks:
      symbols.append(stock["symbol"])


    
    historical_path = os.path.abspath(os.getcwd() + "/../datahut/data/historical/")
    print("historical_path = {}".format(historical_path))

    for symbol in symbols:
      full_path = historical_path + "/" + symbol + "/"

      if not os.path.exists(full_path):
        print("no historical data for " + symbol)
        self.fetch_data(symbol)

      for filename in os.listdir(full_path):
        print(os.path.join(full_path, filename))
        continue
      exit()

      date_parser = pd.to_datetime
      data = pd.read_csv(full_path, parse_dates=["Date"], date_parser=date_parser)



      data.set_index("Date", inplace=True)
      # print(data.index)

      row = data.loc["2012-05-21"]
      print(type(row))
      print(row)
      print(row["Volume"])

  def fetch_data(self, symbol):
    print("[FETAL]fetch_data not implemeted.")
    pass

if __name__ == "__main__":
  loader = expt_loader()

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

  data = loader.load_data()
