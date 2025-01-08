# import smtplib

# my_emmail = "george180594@gmail.com"
# password = "aojrrvbcxmeyshua"


# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_emmail, password=password)
#     connection.sendmail(
#         from_addr=my_emmail,
#         to_addrs="georgelcr@gmail.com",
#         msg="Subject:Hello\n\nThis is the body of my email",
#     )

import datetime as dt

now=dt.datetime.now()
year=now.year
month=now.month
day_of_week= now.weekday()


date_of_birth= dt.datetime(year=1994,month=5,day=18)
print(date_of_birth)