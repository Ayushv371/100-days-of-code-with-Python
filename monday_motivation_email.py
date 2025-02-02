import random
import smtplib
import datetime as dt

SENDER_EMAIL = "******YOUR EMAIL******"
SENDER_PASSWORD = "******YOUR PASSWORD******"
RECIPIENT_EMAIL = "******RECIPIENT EMAIL******"

day = dt.datetime.now().weekday()
print(day)
if day == 0:
    try:
        with open("motivation.txt") as f:
            all_quotes = f.readlines()
            quote = random.choice(all_quotes)
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)
            connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=RECIPIENT_EMAIL,
                                msg=f"Subject:Monday Motivation\n\n{quote}")
    except Exception as e:
        print(e)