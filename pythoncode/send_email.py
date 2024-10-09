# This code will send e-mail which you have coded in the code  
import smtplib, ssl

def sendEmail(message):
	smtp_server = "smtp.gmail.com"
	port = 587 
	sender_email = " ----- Enter your E-mail ------ "
	password = "  ----- Enter your E-mail password ------ "
	receiver_email = " ----- Enter your E-mail ------ "

	context = ssl.create_default_context()

	try:
	    server = smtplib.SMTP(smtp_server,port)
	    server.ehlo() 
	    server.starttls(context=context) 
	    server.ehlo()
	    server.login(sender_email, password)
	    server.sendmail(sender_email, receiver_email, message)
	   
	except Exception as e:
	    print(e)
	finally:
	    server.quit()
