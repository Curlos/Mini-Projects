import urllib3
import time
import smtplib
import ssl
import getpass
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
password = getpass.getpass(
    prompt="Type your email's password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

# Email-related things
sender_email = os.getenv("SENDER_EMAIL")
receiver_email = os.getenv("SENDER_EMAIL")


def checkSiteConnection(url):
    ''' Checks the connection status of the url and returns the http response status code. (i.e. 200 returned if site is up and running)'''
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    return int(r.status)


def checkEveryXSeconds(url, seconds):
    ''' Checks every x amount of seconds to see if the user-inputted website is down. If the site is down, an email is sent to the user informing them the site is currently down.'''
    starttime = time.time()
    while True:
        status = checkSiteConnection(url)
        print(status)
        if(status != 200):
            message = MIMEMultipart()
            message['Subject'] = f"Site Status Update"
            message['From'] = sender_email
            message['To'] = receiver_email

            body = f"We are sorry to inform you but the site: {url} is currently down."

            message.attach(MIMEText(body, 'html'))

            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email,
                                message.as_string())

        time.sleep(seconds - ((time.time() - starttime) % seconds))


checkEveryXSeconds('https://archive.org/', 20)
