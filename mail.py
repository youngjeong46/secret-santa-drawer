import config
import smtplib, ssl
import getpass
from email.mime.text import MIMEText

def mail(sender, receiver, email, wishlist):
  print(sender+" will send the gift to "+receiver+". Here is what they want: "+ wishlist)
  host_email = config.host_email+"@"+config.email_domain
  
  msg = ('From: %s\r\nTo: %s\r\n' % (host_email, email))
  msg = msg + '''Subject: [TEST] You have drawn a name!

  Hi {name}, 
  
  Thank you for participating in the season of gift giving! You are.... {receiver}'s Secret Unicorn! 
  
  Please look at their wish list here: {wishlist}.
  
  Thanks and let's have fun with this!!
  
  Sincerely Yours This Holiday,
  
  Secret Unicorn Host'''
  
  port = 587
  context = ssl.create_default_context()

  user = smtplib.SMTP("smtp.gmail.com", port)
  user.starttls(context=context)
  while True:
    password = getpass.getpass("Type your password and press enter: ")
    try: 
      user.login(host_email,password)
      user.sendmail(host_email,email,msg.format(name=sender,receiver=receiver,wishlist=wishlist))
      user.quit()
    except smtplib.SMTPAuthenticationError:
      print('Login incorrect: Please reenter the password')
      continue
    break

if __name__=="__main__":
  mail("Andrew","Young","test@mail.com","Unicorn Doll, Unicorn Ice Cream, Unicorn Rydes")
  # mail_test()