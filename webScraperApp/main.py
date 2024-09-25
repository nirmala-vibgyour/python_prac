import smtplib
import ssl
import time
import selectorlib
from fetchUrl import getUrl
import sqlite3

connection = sqlite3.connect("data.db")
# "INSERT INTO events VALUES ('Tigers, 'Tiger city', '2088.10.17')"
# "SELECT * FROM events WHERE date='2088.10.16'"


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)['tours']
    return value
# displaytimer


def send_mail(message):
    host = "smtp.gmail.com"
    port = 465

    username = "nirmalacourses@gmail.com"
    password = "sxdcctqftahffbdb"

    receiver = "nirmalawrk@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
    print("Email is sent!")


def store(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES(?, ?, ?)", row)
    connection.commit()


def read(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    band, city, date = row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", (band, city, date))
    rows = cursor.fetchall()
    return rows


if __name__ == "__main__":
    while True:
        scraped = getUrl()
        extracted = extract(scraped)

        if extracted != "No upcoming tours":
            row = read(extracted)
            if not row:
                store(extracted)
                send_mail(message="Hey, new event is found!!")

        time.sleep(2)

