import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "rageandcool@gmail.com"
MY_PASSWORD = "jyug eups ylah zisw"
MY_LAT = 22.565570
MY_LONG = 88.370210

def iss_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude =float(data["iss_position"]["latitude"])

    if MY_LAT-5 <=iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <=MY_LONG+5:
        return True


def isnight():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now>=sunset or time_now<=sunrise:
        return True

while True:
    time.sleep(60)
    if iss_iss_overhead() and isnight():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up \n\nThe ISS is above you in the sky"
        )

