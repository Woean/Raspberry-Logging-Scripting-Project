#!/usr/bin/python3

import datetime
import mysql.connector as mariadb
import plotly
from plotly.graph_objs import Scatter, Layout

#connects to database
mariadb_connection = mariadb.connect(host='localhost', user='werner', password='Scripting', database='templogger')
cursor = mariadb_connection.cursor()
print("connection save")

#sql query
sql = "SELECT * FROM full where ID%2 = 0 ORDER BY ID DESC LIMIT 50"

#creates list for temperature and humidity
temp = list()
time = list()

#reads data from db and stores it to lists
try:
    cursor.execute(sql)
    records = cursor.fetchall()
    print("number of records added for graph: ", cursor.rowcount)
    for row in records:
        temp.append(row[2])
        s = str(row[1])
        time.append(s)
    mariadb_connection.commit()
    print("data succesfully read")
except Exception as e:
    print("error while db operation:", e)
    mariadb_connection.rollback()

mariadb_connection.close()

#creates html file with ploted graph
plotly.offline.plot({
    "data": [Scatter(x=time, y=temp)],
    "layout": Layout(title="Temperaturverlauf zur Zeit")
})



