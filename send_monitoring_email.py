import argparse 
import xml.etree.ElementTree as ET 
import requests
import numpy 
import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date,datetime
today= date.today()
d4 = today.strftime("%b-%d-%Y")


fromaddr = "hikari.code@gmail.com"
toaddr = "hikari.code@gmail.com"
message = MIMEMultipart("alternative")
message["Subject"] = str(d4) + " Daily Report"
message["From"] = fromaddr
message["To"] = toaddr




html = "<ol>"
r=requests.get("https://ldczk.com/state_endpoint/")
with open('./applications.xml','wb') as f1 : 
    f1.write(r.content)
et= ET.parse('./applications.xml')
root= et.getroot();
applications = root.findall('application')

for application in applications  : 
    html+= "<h2"
    color=False
    if ((datetime.now() -  datetime.strptime(str(application.find('update_date').text),'%Y-%m-%d %H:%M:%S')).total_seconds()) / 86400 > 1 : 
        color =True
    if application.find('previous_status').text!='TERMINATED' and application.find('application_status').text!='TERMINATED':
        color=True
    if color :
        html+=" style='color:red;' "
    html+="><li>"+application.find('application_name').text+ "</li></h2><ul>"
    html+= "<pre><li><h3 style='display:inline;'><b><u>Application Status</u>  : </b></h3><div  style='display:inline;'>"+application.find('application_status').text+ "</div></li></pre>"
    html+= "<pre><li><h3 style='display:inline;'><b><u>Previous Status</u>  : </b></h3><div  style='display:inline;'>"+application.find('previous_status').text+ "</div></li></pre>"
    html+= "<pre><li><h3  style='display:inline;' ><b><u>Comment</u>  : </b></h3><div  style='display:inline;'>"+application.find('comment').text+ "</div></li></pre>"
    html+= "<pre><li><h3  style='display:inline;' ><b><u>Update Date</u>  : </b></h3><div  style='display:inline;'>"+application.find('update_date').text+ "</div></pre></li></ul>"

html+='</ol>'

#s = smtplib.SMTP('smtp.gmail.com', 587) 
s = smtplib.SMTP('smtp.elasticemail.com', 2525) 

s.ehlo()
s.starttls() 
s.ehlo()
#s.login('cooperatepvtinc@gmail.com','c00p3r4t3') 
s.login('hikari.code@gmail.com','eedd6938-3151-4955-97e1-7c7a8c6f89b2') 
text="Automatic Mailer"
part1= MIMEText(text,'plain')
part2 = MIMEText(html, "html")
message.attach(part1)
message.attach(part2)
s.sendmail(fromaddr, toaddr, message.as_string()) 
  
s.quit() 
    
