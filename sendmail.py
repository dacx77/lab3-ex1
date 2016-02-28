import smtplib

fromname = 'Dacx'
toname = 'Dacx Pro'
fromaddr = 'dacx77@gmail.com'
toaddr  = 'dacxproductionsja@gmail.com'
subject = 'Test'
msg = 'Hello World'
message = """From: {} <{}>
To: {} <{}>
Subject: {}

{}
"""
messagetosend = message.format(
                             fromname,
                             fromaddr,
                             toname,
                             toaddr,
                             subject,
                             msg)

# Credentials (if needed)
username = 'dacx77@gmail.com'
password = 'pldvmqjwmedemezr'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddr, messagetosend)
server.quit()