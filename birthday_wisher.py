import pandas as pd
import smtplib
import datetime as dt
date = dt.datetime.now()
df = pd.read_csv("birthdays.csv")
birthdays = df.to_dict(orient="records")
EMAIL = "ayushvapptester@gmail.com"
PASSWORD = "**********"
today = date.day
month = date.month
YEAR = date.year
for person in birthdays:
    if person["month"] == month and person["day"] == today:
        with open("wish1.txt") as f:
            content = f.readlines()
            letter = "".join(content)
            letter = letter.replace("[NAME]", person["name"])
            letter = letter.replace("[AGE]", str(YEAR-person["year"]))
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=EMAIL, password=PASSWORD)
                connection.sendmail(from_addr=EMAIL, to_addrs=person["email"],
                                    msg=f"Subject:Happy Birthday!\n\n{letter}")