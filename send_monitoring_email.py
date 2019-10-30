import argparse 
import xml.etree.ElementTree as ET 
import requests
import numpy 
import smtplib 
'''
r=requests.get("https://ldczk.com/state_endpoint/")
et= ET.parse(r.content)
root= ET.getroot();
root.findall('application')
'''

#s = smtplib.SMTP('smtp.gmail.com', 587) 
s = smtplib.SMTP('aspmx.l.google.com', 25) 

s.ehlo()
s.starttls() 
s.ehlo()
#s.login('cooperatepvtinc@gmail.com','c00p3r4t3') 
#s.login('cooperatepvtinc@gmail.com','bb65194c-4aea-4643-b4e9-15bd76038a30') 

fromaddr = "cooperatepvtinc@gmail.com"
toaddr = "faltushiv9@gmail.com"
message = "Subject: Information Regarding Mail \n\n Mail is working to unsubscribe please wait"
s.sendmail(fromaddr, toaddr, message) 
  
s.quit() 
