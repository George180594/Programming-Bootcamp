import datetime as dt
import smtplib
import random



    

#import txt and transform to a list
def import_text():
    with open("day_32/quotes.txt","r") as data:
        data_text=data.readlines()
    choosen_line= random.choice(data_text)
    return choosen_line


def send_email(choosen_line):
    # Sending email
    my_emmail = "george180594@gmail.com"
    password = "aojrrvbcxmeyshua"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_emmail, password=password)
        connection.sendmail(
            from_addr=my_emmail,
            to_addrs="georgelcr@gmail.com",
            msg=f"Subject:Happy day\n\n{choosen_line}",
        )




now=dt.datetime.now()
weekday=now.weekday()
if weekday==3:
    choosen_line= import_text()
    send_email(choosen_line=choosen_line)