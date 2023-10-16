import smtplib
import pandas
import random
import datetime as dt

MY_ADDRESS = "your mail address"
PASSWORD = "your app password"

# use app password. For gmail turn on 2 steps verification then app password option will show and create one

now = dt.datetime.now()
today_day = now.day
today_month = now.month
today = (today_month, today_day)

#fill info in csv file with proper parameter

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = (f"./letter_templates/letter_{random.randint(1, 5)}.txt")
    with open(file_path) as letter_file:
        contents = letter_file.read()
        final_contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_ADDRESS, PASSWORD)
        connection.sendmail(from_addr=MY_ADDRESS,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject: Happy Birthday\n\n {final_contents} ")


"""to automated this program creata account on https://www.pythonanywhere.com/ for free
then add main.py and birthdats.csv file 
add new directoey named as letters_templates and add all the letter files
then select console -> Bash -> Run
code:
python3 main.py
if have any error go the the error and fild a referance and copy and paest on browser and give the access
then run the program again with 
python3 main.py

to set time : Go to dashborad , select Tasks -> Set Schedule  enter same commend : python3 main.py
then set the time as UTC [find your UTC time from google]

Finished. This program will run everyday on that time and send a mail if matched onn that day.
Thank you"""