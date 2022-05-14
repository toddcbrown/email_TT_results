import pandas as pd
import email_

df = pd.read_csv('22_Roster_JD_TT.csv')

email_.email(df,df['May_21'],test_email='temego6968@roxoas.com')