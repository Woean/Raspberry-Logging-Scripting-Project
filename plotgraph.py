import datetime
import mysql.connector as mariadb
import plotly
from plotly.graph_objs import Scatter, Layout


mariadb_connection = mariadb.connect(host='localhost', user='werner', password='Scripting', database='templogger')
cursor = mariadb_connection.cursor()
print("connection save")

sql = "SELECT * FROM full where ID%7 = 0 ORDER BY ID DESC LIMIT 50"

temp = list()
time = list()

cursor.execute(sql)
records = cursor.fetchall()
print(cursor.rowcount)
for row in records:
    temp.append(row[2])
    s = str(row[1])
    time.append(s)
mariadb_connection.commit()

print(temp)
print(time)

plotly.offline.plot({
    "data": [Scatter(x=time, y=temp)],
    "layout": Layout(title="Temperaturverlauf zur Zeit")
})



