#!/usr/bin/env python
#THIS IS A SIMPLE PYTHON SCRIPT FOR BACKING UP CISCO IOS ROUTER CONFIG
#This type of script is mainly executable in Debain based Linux.
#Install Paramiko module using "pip"
#Also, install TFTP server on debian.
#I have used GNS3 for emulating the router.... 
# make this script executable by using "chmod +x router_script.py"

#@@@@@@@@@@   WARNING: Please review the script and setup the parameters accordingly    @@@@@@@@
#@@@@@@@@@@   BEFORE DEPLOYING into PRODUCTION NETWORKS.                                @@@@@@@@

import paramiko         #importing this module for making SSH connection into device
import sys
import re
import time
import getpass          # masking the password 

def open_ssh_conn(ip):
  # Try-except block in order to catch the exception of wrong username and password
	try:
	#ask for username, you don't want username to be default
		username = raw_input("Username: ")

	#ask for password, and mask it

		password = getpass.getpass()
	
		
	#open session using Paramiko
		session = paramiko.SSHClient()
	
	#allow auto-add user policy even if no host keys are configured/implemented
	
		session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	 
	#passing the necessary paramaters

		session.connect(ip, port=22, username = username, password = password)
		
	#start the shell
				
		connection = session.invoke_shell()
		output = connection.recv(65535)
		
	#TFTP Server
		tftp_server = raw_input("IP address of TFTP-server? ")
		#tftp_server = "X.X.X.X" #Directly state your own TFTP server IP instead of asking repeatedly

	#Ask Destination file
		dest_file = raw_input("Destination file name? ")
		time.sleep(1)
	#enter into privelege mode from user mode
		connection.send("enable")
		connection.send("\n")
		time.sleep(1)
	#Execute command

		connection.send("copy startup-config tftp://"+str(tftp_server))
		connection.send("\n")   #sending  above command
		

		output += connection.recv(65535)
		print ''.join(output)
		time.sleep(1)
		output += connection.recv(65535)
		print "".join(output)		
		connection.send("\n")   #sending the confirmation from router for (Remote address []?)
		time.sleep(1)
		output += connection.recv(65535)
		print "".join(output)						
		connection.send(dest_file)
		time.sleep(1)
		
		connection.send("\n")
	
		
		time.sleep(1)
		output += connection.recv(65535)
		print "".join(output)		
		session.close()
		time.sleep(1)

		print "Backup sucessful....Exiting...Please wait"

	except paramiko.AuthenticationException:
	        print "Invalid Username or password"
	        print "Closing program...\n"
	
#calling SSH Function
print("########################################################################")
print("####################### ROUTER BACKUP SCRIPT ###########################")
print("########################################################################") 

IP_address = raw_input("Enter the IP address of the device: ")
open_ssh_conn(IP_address)

