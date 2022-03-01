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


def gender(x,categories):
  """
  x = list of categories
  categories = list of girl categories
  """
  gend = list()
  for i in x:
    if i in categories:
      gend.append('F')
    else:
      gend.append('M')
  return gend
  
def sec_to_min(x):
  import pandas as pd
  return str(pd.to_timedelta(x,'s')).split(' ')[2].split('.')[0]