import pandas as pd
import numpy as np
import email_

df = pd.read_csv('7th_tt_times.csv')

email_.email(df[:5],df['May_21'])