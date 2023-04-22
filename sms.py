# import the lib
import urllib2
import cookielib
from getpass import getpass

# userID, password are based on your credential
username = "userID" 
passwd = "password"

# Read IV Trip Level Idicator from log 
f=open('/home/pi/IVTrip/log.txt','r')
data=f.read()
f.close()
message = data

# Target Mobile Number 
number = ["MobileNumber"]
message = "+".join(message.split(' '))
url = 'http://site24.way2sms.com/Login1.action?'
data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]

try:
    usock = opener.open(url, data)
except IOError:
    print "Error while logging in."
for i in number:
    jession_id = str(cj).split('~')[1].split(' ')[0]
    send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
    send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+i+'&message='+message+'&msgLen=136'
    opener.addheaders = [('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
    try:
        sms_sent_page = opener.open(send_sms_url,send_sms_data)
    except IOError:
        print "Error while sending message"
    print "SMS has been sent."
