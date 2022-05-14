import pandas as pd
import numpy as np

def sec_to_min(x):
  """
  converts integer seconds to timedelta format HH:MM:SS
  """
  return str(pd.to_timedelta(x,'s')).split(' ')[2].split('.')[0]
  
def conv_to_sec(x):
  """
  Converts string time to integer seconds
  """
  j = str(x).split(':')
  if len(j) == 2:
    sec = int(j[0])*60 + int(j[1])
    return sec
  elif len(j) < 2:
    return int(0)
  else:
    sec = int(j[0])*60*60 + int(j[1])*60 + round(float(j[2]))
    return int(sec)


def mean_tt_time(x):
  """
  x: a list of string times 
  this turns a list of string times into integer seconds and back to MM:SS
  """
  return sec_to_min(np.mean([(conv_to_sec(i)) for i in x]))