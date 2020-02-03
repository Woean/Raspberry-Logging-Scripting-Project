#!/usr/bin/python3

from datetime import datetime
import Adafruit_DHT
import mysql.connector as mariadb
from smtplib import SMTP
from email.message import EmailMessage
import re

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

mariadb_connection = mariadb.connect(host='localhost', user='werner', password='Scripting', database='templogger')
cursor = mariadb_connection.cursor()
print("connection save")

humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)


def validate(input):

    inputstr  = str(input)
    reg = "^[0-9]+\.?[0-9]*$"
    x = False
    pat = re.compile(reg)
    mat = re.search(pat, inputstr)
    if mat:
        print("Passwd is valid")
        x = True
        return x
    else:
        print("not valid")
        return x


if validate(humidity) == True and validate(temperature) == True:
    
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    print(timestamp)

    formatted_date = now.strftime('%Y-%m-%d')
    formatted_time = now.strftime('%H:%M:%S')
    cursor.execute("INSERT INTO full(Date,Time,Temperature, Humidity) VALUES (%s, %s, %s, %s)",(formatted_date, formatted_time, temperature, humidity))
    mariadb_connection.commit()
    print("Temp: ",(temperature))
    print("Hum: ",(humidity))
else:
    print("Failed to retrieve data from humidity sensor")

SENDER = 'rasp_logger@gmx.at'
RECIPENT = 'werner.haingartner@gmail.com'
SMTP_USER = SENDER
SMTP_PASS = 'Trz/2vsC'
SMTP_HOST = 'mail.gmx.net'
SMTP_PORT = '587'

warning = "Achtung, ihr Raspberry hat am {} um {} folgende Temperatur über 25°C gemessen: {}".format(formatted_date, formatted_time, temperature) 

msg = EmailMessage()
msg.set_content(warning)
msg['Subject'] = 'Temperaturwarnung'
msg['From'] = SENDER
msg['To'] = RECIPENT

if temperature > 25:
    try:
        with SMTP(host=SMTP_HOST, port=SMTP_PORT) as smtp:
            smtp.starttls()
            smtp.login(SMTP_USER, SMTP_PASS)
            smtp.send_message(msg)
    except Exception as e:
        print('oh no failure')
        print(e)
        exit(1)
else:
    print("no warning sent per mail")

