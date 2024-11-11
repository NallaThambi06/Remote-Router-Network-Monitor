# Router_Network_Monitor
This Project aims to monitor the router's internet connection and reachable status from anywhere in the world(remotely), this notifies the client/user using the sms where we use the Twilio SMS gateway. We can also configure the router's static IP, name of the router, and client/user inbound or receiving number.
# Table of contents
1. Installation
2. Required Libraries
3. Configuration
4. Additional details
# Installation
***Installation is easy because this git file contains executable and Python files for reference.<br/>
***After extracting the git file, configure the python file per your requirements and delete all other files excluding "Final_TEST.py".<br/>
***Configuring the Python file use the "PyInstaller" library to convert them to executable file.<br/>
### CMD on <your_py-path> <br/>
>pyinstaller <file_name>
# Required Libraries
--import ping (from ping3)<br/>
--import Client (from twilio.rest)<br/>
--import speedtest<br/>
# Configuration
***Create a free trial account for the testing in "Twilio sms gateway" which provides $15 and it costs $0.082 per sms and approx $1.32 for the virtual number that is used by the script to send the sms.<br/>
***Locate your account page and copy the **auth_token, account_sid, and twilio_viritual_number**, paste it your code.<br/>
***Get the Static IP address of the router from the service provider or **https://whatismyipaddress.com/**.<br/>
***Add the client mobile number with its prefix(country code) in the script.<br/>
# Additional details
***you can automatically trigger the Python file in the windows task scheduler on the central pc or the server as per your timing requirements.<br/>
***This project helps the system administrator who maintains the cloud servers and web server because the internet connection's status should be known to switch other networks.<br/>
***You can also provide the multiple router's IP address to get any reachable router.<br/>
***If you use network bridge balance automatically with multiple routers, this project will not be effective because this script helps the user to notify about the router's status to switch the network router for the backup.
### Windows Task Scheduler
>**Trigger option** <br/>
program path --- paste the path of the python.exe.<br/>
Add arguments(optional) --- paste the python file name (eg:simple.py)<br/>
start in(optional) --- paste your python file path (eg:C:\Users\HARI\Desktop\DESKTOP\FILES\Python workspace\) **Don't add file name**

