#!/bin/python

from bs4 import BeautifulSoup as bs4
import requests
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

fromaddr = "<YOUR GMAIL EMAIL ADDRESS>" 
toaddr = "<DESIRED EMAIL ADDRESS>"

msg = MIMEMultipart()

# Turn on "Less Secure App for Google accounts. Refer - https://support.google.com/accounts/answer/6010255?hl=en"

msg['From'] = fromaddr
msg['To'] = toaddr

#Make text file in the same directory for storing current value and avoid repititive emails.

PATH_INPUT = "/<Whatever directory>/current_ip.txt"

get_request = requests.get("http://www.ipvoid.com")
soup = bs4(get_request.content,'lxml')
current_ip = soup.find('input', {'name':''})['value']
print "Current IP is " + current_ip

with open(PATH_INPUT, "r") as f:
	existing_IP = f.readlines()
	for line in existing_IP:
		existing_IP = str(line).strip('\n')
	f.close()

if existing_IP == current_ip:
	print "no email sent!"

else:
	msg['Subject'] = "Current IP is " + current_ip
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login(fromaddr, '<PASSWORD>')  #logins
	text = msg.as_string()
	
	server.sendmail(fromaddr, toaddr, text) #sends email
	
	with open(PATH_INPUT, "w") as f:
		f.write(str(current_ip + "\n"))
		f.close()
