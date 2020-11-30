import pandas as pd 
from os import path, makedirs

parse_dates = ['Date']

class dfWriterBase:
  def writeDfTo(self, base_path='', data_frame=pd.DataFrame()):
    lines_num = data_frame.shape[0]

    if lines_num <= 0 or base_path == '':
      print('empty data_frame/base_path input! return..')
      return

    if not path.exists(base_path):
      makedirs(base_path)

    last_filename = data_frame.loc[0]['Date'].strftime('%Y%m')
    last_index = 0
    for i in range(1, lines_num):
      curr_filename = data_frame.loc[i]['Date'].strftime('%Y%m')
      if last_filename != curr_filename or i >= lines_num - 1:
        filepath = base_path + last_filename + '.csv'
        end_index = lines_num if i >= lines_num - 1 else i
        
        if not path.exists(filepath):
          file_ptr = open(filepath, "w")
          data_frame[last_index:end_index].to_csv(index=False, path_or_buf=file_ptr, date_format='%Y-%m-%d-%H-%M-%S')
          file_ptr.close()
        else:
          self.appendDfToFullPath(filepath, data_frame[last_index:end_index])

        last_index = i
        last_filename = curr_filename

  def appendDfToFullPath(self, full_path='', data_frame=pd.DataFrame()):
    if data_frame.shape[0] <= 0 or full_path == '':
      print('empty data_frame/full_path input! return..')
      return

    date_parser = pd.to_datetime
    old_content = pd.read_csv(full_path, parse_dates=parse_dates, date_parser=date_parser)
    
    # suppress the chained assignment warning, expected here
    pd.set_option('mode.chained_assignment', None)
    data_frame['Date'] = pd.to_datetime(data_frame['Date'], utc=True)
    pd.set_option('mode.chained_assignment', 'raise')

    result = pd.concat([old_content, data_frame])

    # sorting by Date
    result.sort_values("Date", inplace = True)
      
    # dropping ALL duplicte values
    result.drop_duplicates(subset ="Date", keep = 'first', inplace = True)

    old_num = old_content.shape[0]
    new_num = result.shape[0]

    if new_num > old_num:
      file_ptr = open(full_path, "w")
      result.to_csv(index=False, path_or_buf=file_ptr)
      file_ptr.close()

