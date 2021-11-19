import smtplib
import random

# Open file and split it into pieces and choose a random day
with open("Daily-Stoic.txt") as file:
    chapter = file.read()
    daily_list = chapter.split("\n\n\n\n\n")
    random_daily_list = random.choice(daily_list)

# Send Emails and be happy
a = random_daily_list.split('\n')
print(a[3])