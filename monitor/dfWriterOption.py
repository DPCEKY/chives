import pandas as pd
from os import path, makedirs

parse_dates = ["Date"]


class dfWriterOption:
  def writeDfTo(self, base_path="", data_frame=pd.DataFrame(), option_name=""):
    lines_num = data_frame.shape[0]

    if lines_num <= 0 or base_path == "" or option_name == "":
      print("empty data_frame/base_path/option_name input! return..")
      return

    if not path.exists(base_path):
      makedirs(base_path)

    filepath = base_path + option_name + ".csv"
    if not path.exists(filepath):
      file_ptr = open(filepath, "w")
      data_frame.to_csv(
        index=True,
        path_or_buf=file_ptr,
        date_format="%Y-%m-%d",
      )
      file_ptr.close()
    else:
      print("option data already stored. return..")
      return
