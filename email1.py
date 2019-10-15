
import smtplib
from email.mime.text import MIMEText

# set up the SMTP server
MAIL_PORT=587
MAIL_SERVER= 'localhost'


def sendMail(SUBJECT,MESSAGE):
	FROM = 'salsa'
	TO = ['salsa']
	try:
		s = smtplib.SMTP(MAIL_SERVER)
		s.sendmail(FROM, TO, MESSAGE)
		print "Successfully sent email"
	except SMTPException:
		print "Error: unable to send email"

sendMail('fail test', 'test')

