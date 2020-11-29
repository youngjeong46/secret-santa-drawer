import config
import smtplib
import ssl
import getpass
import sys
from time import sleep


def mail(sender, receiver, email, wishlist):
    print(sender + " will send the gift to "+receiver+". Here is what they want: " + wishlist)
    host_email = config.host_email + "@" + config.email_domain

    msg = ('From: %s\r\nTo: %s\r\n' % (host_email, email))
    msg = msg + '''Subject: [SECRET UNICORN] You have drawn a name!

    Hi {name}, 

    Thank you for participating in the season of gift giving! You are.... {receiver}'s Secret Unicorn! 

    Please look at their wish list: {wishlist}.

    Thanks and let's have fun with this!!

    Sincerely Yours This Holiday,

    Secret Unicorn Host'''

    port = 587
    context = ssl.create_default_context()

    user = smtplib.SMTP("smtp.gmail.com", port)
    user.starttls(context=context)

    print("Sending email to "+sender+" at "+email+", using the host email: "+host_email+".\n")
    while True:
        if config.pass_word:
            password = config.pass_word
        else:
            password = getpass.getpass("Type your password and press enter: ")
        try:
            print("Logging in...")
            for i in range(21):
                sys.stdout.write('\r')
                # the exact output you're looking for:
                sys.stdout.write("[%-20s] %d%%" % ('=' * i, 5 * i))
                sys.stdout.flush()
                sleep(0.05)
            print("")
            user.login(host_email, password)
            user.sendmail(host_email, email, msg.format(name=sender, receiver=receiver, wishlist=wishlist))
            user.quit()
        except smtplib.SMTPAuthenticationError:
            if config.pass_word:
                sys.exit('Login incorrect: Please check your config file.')
            print('Login incorrect: Please re-enter the password')
            continue
        break


if __name__ == "__main__":
    mail("Andrew", "Young", "test@mail.com", "Unicorn Doll, Unicorn Ice Cream, Unicorn Rydes")
    # mail_test()