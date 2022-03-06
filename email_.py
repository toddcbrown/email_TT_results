import yagmail
import convert
import numpy as np
import pandas as pd
def email(df,lastTT,compare_TT=None):
  """
  **Must use following columns in df
  ['Name','Last','email_rider','email_parent','Cat', 'May_21','June_21','July_21','Aug_21','May_22','June_22','July_22','Aug_22']
  """
  df = df.replace('',int(0))
  sender = 'skyridge.mtb.tt.results@gmail.com'
  password = 'uqrs dxjs vpos ixcw'
  yag = yagmail.SMTP(user=sender,password=password)
  todays_mean = convert.mean_tt_time([i for i in lastTT if i != 0])
  for i in df.index:
    Name = df['Name'].iloc[i]
    recepient_rider = df['email_parent'].iloc[i]
    recepient_parent = df['email_parent'].iloc[i]
    subject = "Skyridge Junior Devo MTB Team | %s TT Results"%(Name)
    Name = df['Name'].iloc[i]
    recepient_rider = df['email_rider'].iloc[i]
    recepient_parent = df['email_parent'].iloc[i]
    subject = "Skyridge JD MTB Team | %s TT Results"%(Name)
    contents = """%s's TT results are:\n-----------
    MAY 2021: %s
    JUNE 2021: %s
    JULY 2021: %s
    AUG 2021: %s

    MAY 2022: %s
    JUNE 2022: %s
    JULY 2022: %s
    AUG 2022: %s

    If you believe this is incorrect please text me at (801)669-2560.
    These results are weighed heavily on deciding practice groups. \n\n
    Time trials can be made up using <a href="https://www.strava.com/segments/15283565"> this Strava segment</a>. Please notify a coach if you decide to do this. Also we will add 4 percent to the time because it does not cover the full loop.
    
    --------------
    The following is for your FYI, you can choose wether to share it with your child:
    Today's average time was %s.
    
    Thanks!
    Coach Todd"""%(Name,
                   df['May_21'].iloc[i],
                   df['June_21'].iloc[i],
                   df['July_21'].iloc[i],
                   df['Aug_21'].iloc[i],
                   df['May_22'].iloc[i],
                   df['June_22'].iloc[i],
                   df['July_22'].iloc[i],
                   df['Aug_22'].iloc[i],
                   todays_mean)
    
    contents_rider = """Your TT results are:\n-----------
    MAY 2021: %s
    JUNE 2021: %s
    JULY 2021: %s
    AUG 2021: %s

    MAY 2022: %s
    JUNE 2022: %s
    JULY 2022: %s
    AUG 2022: %s

     
    Thanks!
    Coach Todd"""%(
                   df['May_21'].iloc[i],
                   df['June_21'].iloc[i],
                   df['July_21'].iloc[i],
                   df['Aug_21'].iloc[i],
                   df['May_22'].iloc[i],
                   df['June_22'].iloc[i],
                   df['July_22'].iloc[i],
                   df['Aug_22'].iloc[i])
    
    try:
      yag.send(to=recepient_rider,subject=subject,contents=contents_rider)
    except:
      print(Name + ' rider email failed')
    try:
      yag.send(to=recepient_parent,subject=subject,contents=contents)
    except:
      print(Name + ' parent email failed')
    print('.')