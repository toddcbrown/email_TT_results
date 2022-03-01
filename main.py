import pandas as pd
import numpy as np
import yagmail 
import convert
#import email




######################################

columns = ['Name','Last','email_rider','email_parent','Cat', 'May_21','June_21','July_21','Aug_21','May_22','June_22','July_22','Aug_22']
one = ['Freddie', 'Mercury','feddy@mymail.com','xirix46505@sueshaw.com','Adv B','40:05','38:55','37:21','32:15','37:44','','','']
two = ['Kate', 'Spade','feddy@mymail.com','xirix46505@sueshaw.com','Beg G','','','','','47:44','','','']
df = pd.DataFrame([one,two])
df.columns = columns

df['June_21'] = df['June_21'].apply(convert.conv_to_sec)
find_mean = np.mean(df['June_21'].loc[(df['June_21'] > 0)])
print(convert.sec_to_min(np.mean(find_mean)))



email(df,df['July_22'])