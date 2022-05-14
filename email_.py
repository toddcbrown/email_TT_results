import yagmail
import convert
import numpy as np
import pandas as pd
import time
def email(df,lastTT,test_email=None):
  """
  **Must use following columns in df
  ['Name','Last','email_rider','email_parent','Cat', 'May_21','June_21','July_21','Aug_21','May_22','June_22','July_22','Aug_22']
  """
  #lastTT is the "current TT that you want statistics on"
  lastTT = lastTT.replace(['',np.nan,'DNF','nan'],int(0))
  lastTT = [convert.conv_to_sec(x) for x in lastTT]
  todays_mean = np.mean([x for x in lastTT if x != 0])
  todays_mean = convert.sec_to_min(todays_mean)
  #replace NaN with "no result"
  df = df.replace(['',np.nan,'DNF','nan'],'no result')
  #Prime yagmail 
  sender = 'skyridge.mtb.tt.results@gmail.com'
  password = 'spfb fmbe rmqp etmy'
  yag = yagmail.SMTP(user=sender,password=password)

  #Go through each line and send email 
  for i in df.index:
    Name = df['Name'].iloc[i]
    #Allow for testing 
    if test_email is None:
      recepient_rider=print('email protected with#') #df['email_rider'].iloc[i]
      recepient_parent =print('email protected with#')#df['email_parent'].iloc[i]
    else:
      recepient_rider=test_email
      recepient_parent=test_email 
    
    subject = "Skyridge Junior Devo MTB Team | %s TT Results"%(Name)
    category = df['Cat'][i]
    if category == '8 Male' or category == '8 Female':
      
      contents = open('parent8th.txt','r').read()%(Name,
                     df['May_21'].iloc[i],
                     df['June_21'].iloc[i],
                     df['July_21'].iloc[i],
                     df['Aug_21'].iloc[i],
                     df['May_22'].iloc[i],
                     df['June_22'].iloc[i],
                     df['July_22'].iloc[i],
                     df['Aug_22'].iloc[i],
                     todays_mean)
      contents_rider = open('rider8th.txt','r').read()%(
                   df['May_21'].iloc[i],
                   df['June_21'].iloc[i],
                   df['July_21'].iloc[i],
                   df['Aug_21'].iloc[i],
                   df['May_22'].iloc[i],
                   df['June_22'].iloc[i],
                   df['July_22'].iloc[i],
                   df['Aug_22'].iloc[i])  
    else:
      contents = open('parent7th.txt','r').read()%(Name,
                     df['May_22'].iloc[i],
                     df['June_22'].iloc[i],
                     df['July_22'].iloc[i],
                     df['Aug_22'].iloc[i],
                     todays_mean)
      contents_rider = open('rider7th.txt','r').read()%(
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
    print(Name+' email sent')
    
    #TIME DELAY TO ALLOW BULK MESSAGE SENDING
    time.sleep(15)