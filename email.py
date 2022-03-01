def email(df,lastTT,compare_TT=None):
  import pandas as pd
  import convert
  print(df.head())
  """
  **Must use following columns in df
  ['Name','Last','email_rider','email_parent','Cat', 'May_21','June_21','July_21','Aug_21','May_22','June_22','July_22','Aug_22']
  """
  sender = 'boor3657@gmail.com'
  password = 'hnfe wank biyc cwul'
  yag = yagmail.SMTP(user=sender,password=password)
  todays_mean = convert.sec_to_min(
    np.mean(
      lastTT.apply(
        convert.conv_to_sec.loc[lastTT.apply(conv_to_sec) > 0]))
  for i in df.index:
    Name = df['Name'].iloc[i]
    recepient_rider = df['email_parent'].iloc[i]
    recepient_parent = df['email_parent'].iloc[i]
    subject = "Skyridge Junior Devo MTB Team | %s TT Results"%(Name)
    contents = """%s's TT results are
    MAY 2021: %s
    JUNE 2021: %s
    JULY 2021: %s
    AUG 2021: %s
    
    MAY 2022: %s
    JUNE 2022: %s
    JULY 2022: %s
    AUG 2022: %s
    
    If you believe this is incorrect please text me at (801)669-2560.
    These results are weighed heavily on deciding practice groups.
    If you feel the need to have a makeup then you can talk to a coach and use Strava.
    
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
    
    yag.send(to=recepient_parent,subject=subject,contents=contents)
    print('%s email sent'% recepient_rider)