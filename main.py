import pandas as pd
import numpy as np
import yagmail 
import convert
import email_

columns = ['Name','Last','email_rider','email_parent','Cat', 'May_21','June_21','July_21','Aug_21','May_22','June_22','July_22','Aug_22']
one = ['Freddie', 'Mercury','reltudukki@vusra.com','reltudukki@vusra.com','Adv B','40:05','38:55','37:21','32:15','37:44','','','']
two = ['Kate', 'Spade','reltudukki@vusra.com','reltudukki@vusra.com','Beg G','','','','','47:44','','','']
df = pd.DataFrame([one,two])
df.columns = columns






email_.email(df,df['May_22'])