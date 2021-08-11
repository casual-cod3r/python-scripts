Send your current home IP to your EMAIL (NO Dynamic DNS or Business ISP Plan needed)

Simply spin your Raspberry-Pi for this or any linux running 24x7 in your home/lab.

Script sends email if there is change in IP. You can run script using Cron job every hour or 4 hours (as most of DHCP leases are for 8 hours)

Script can be used for VPN purpose if you don't have Dynamic DNS or Business ISP Plan. Even I believe INTERNET should be completelty FREE Haha!

Cron:

0 1 * * * /usr/bin/python /home/whats_my_ip_script.py
