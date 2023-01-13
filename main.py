##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import random
import pandas
birthday_month = 0
birthday_day = 0
name = ""
birthday_email = ""
my_email = ""
password = ""
birthday_letter = ""

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day

data = pandas.read_csv("birthdays.csv")
birthday_dict = data.to_dict(orient="records")
for birthdays in birthday_dict:
    if birthdays["month"] == month and birthdays["day"] == day:
        birthday_month = birthdays["month"]
        birthday_day = birthdays["day"]
        name = birthdays["name"]
        birthday_email = birthdays["email"]
        print("Its someones birthday.")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
letter_template = "./letter_templates/letter_"+str(random.randint(1, 3))
with open(f"{letter_template}.txt", "r") as file:
    letter = file.readlines()
    replace_name = letter[0].replace("[NAME]", name)
    letter[0] = replace_name
    birthday_letter = "".join(letter)

# 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_email,
            msg=f"Subject:Happy Birthday!\n\n{birthday_letter}")



