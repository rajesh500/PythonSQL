# import required packages
import pandas as pd
import datetime
import smtplib
import time
import requests

from win10toast import ToastNotifier

# your gmail credentials here
GMAIL_ID = 'rajeshjkv5@gmail.com'
GMAIL_PWD = 'lucky1@A'

# for desktop notification
toast = ToastNotifier()
 
# define a function for sending email
def sendEmail(to, sub, msg):
   
    # connection to gmail
    gmail_obj = smtplib.SMTP('smtp.gmail.com', 587)
     
    # starting the session
    gmail_obj.starttls()    
     
    # login using credentials
    gmail_obj.login(GMAIL_ID, GMAIL_PWD)  
     
    # sending email
    gmail_obj.sendmail(GMAIL_ID, to,
                   f"Subject : {sub}\n\n{msg}")
     
    # quit the session
    gmail_obj.quit() 
     
    print("Email sent to " + str(to) + " with subject "
          + str(sub) + " and message :" + str(msg))
     
    toast.show_toast("Email Sent!" ,
                     f"{name} was sent e-mail",
                     threaded = True,
                     icon_path = None,
                     duration = 6)
 
    while toast.notification_active():
        time.sleep(0.1)
		

# driver code
if __name__=="__main__":
   
      # read the excel sheet having all the details
    dataframe = pd.read_excel("excelsheet.xlsx")  
     
    # today date in format : DD-MM
    today = datetime.datetime.now().strftime("%d-%m")
     
    # current year in format : YY
    yearNow = datetime.datetime.now().strftime("%Y")
     
    # writeindex list
    writeInd = []                                                  
 
    for index,item in dataframe.iterrows():
       
        msg = "Many Many Happy Returns of the day dear " + str(item['NAME'])
                
        # stripping the birthday in excel
        # sheet as : DD-MM
        bday = item['Birthday'].strftime("%d-%m")       
         
        # condition checking
        if (today == bday) and yearNow not in str(item['Year']):   
             
            # calling the sendEmail function
            sendEmail(item['Email'], "Happy Birthday",
                      msg)   
             
            # calling the sendsms function
            sendsms(item['Contact'], msg, item['NAME'],
                    "Happy Birthday")  
             
            writeInd.append(index)                                 
 
    for i in writeInd:
       
        yr = dataframe.loc[i,'Year']
         
        # this will record the years in which
        # email has been sent
        dataframe.loc[i,'Year'] = str(yr) + ',' + str(yearNow)            
 
    dataframe.to_excel('excelsheet.xlsx',
                index = False)