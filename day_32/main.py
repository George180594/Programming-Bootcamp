##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime
import smtplib
import random


my_emmail = "george180594@gmail.com"
password = "aojrrvbcxmeyshua"

today = datetime.datetime.now()
today_tuple = (today.month, today.day)


PATH = "day_32/birthdays.csv"
data = pd.read_csv(PATH)


birthday_dict = {
    (data_row["month"], data_row["day"]): data_row
    for (index, data_row) in data.iterrows()
}



if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"day_32/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path, "r") as letter_file:
        contents = letter_file.read()
        contents=contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_emmail, password)
        connection.sendmail(
            from_addr=my_emmail,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthaday!\n\n{contents}"
        )
