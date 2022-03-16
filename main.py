import pandas as pd
import numpy as np
#import yagmail 
#import convert
import email_

df = pd.read_csv('7th_tt_times.csv')

email_.email(df,df['May_21'])