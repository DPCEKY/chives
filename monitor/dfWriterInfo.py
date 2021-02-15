import pandas as pd
from os import path, makedirs

parse_dates = ["Date"]


class dfWriterInfo:
  def writeDfTo(self, base_path="", data_frame=pd.DataFrame(), mode=""):
    if data_frame.shape[0] <= 0 or base_path == "":
      print("empty data_frame/base_path input! return..")
      return

    info = ""
    if mode == "bs":
      info = "balance_sheet"
    elif mode == "qbs":
      info = "quarterly_balance_sheet"
    elif mode == "cf":
      info = "cashflow"
    elif mode == "qcf":
      info = "quarterly_cashflow"

    if len(info) <= 0:
      print("invalid info mode! supported mode: bs, qbs, cf, qcf. returning...")
      return

    if not path.exists(base_path):
      makedirs(base_path)

    filepath = base_path + info + ".csv"
    if not path.exists(filepath):
      file_ptr = open(filepath, "w")
      data_frame.to_csv(
        index=True,
        path_or_buf=file_ptr,
      )
      file_ptr.close()
    else:
      old_content = self.readDfFrom(filepath)

      comb_content = pd.concat([data_frame, old_content], axis=1)
      deduped_content = comb_content.loc[
        :, ~comb_content.columns.duplicated()
      ].sort_index(axis=1)

      file_ptr = open(filepath, "w")
      deduped_content.to_csv(index=True, path_or_buf=file_ptr)
      file_ptr.close()

  def readDfFrom(self, full_path):
    content = pd.read_table(
      full_path, sep=",", index_col=0, header=0, lineterminator="\n"
    )
    content.columns = pd.to_datetime(content.columns)

    return content
