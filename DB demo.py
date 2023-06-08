import mysql.connector

from utilities.configuration import *

# host, database_name, password
# mysql connector established the connection to the database

# conn = mysql.connector.connect(host='localhost',database='PythonAutomation',
#                         user='root',password='root')
conn = getConnection()
print(conn.is_connected())

# create the streamline between the database using cursor

cursor = conn.cursor()
cursor.execute('select * from CustomerInfo')
# row = cursor.fetchone()
# print(row)
# print(row[3])
#
# rowAll = cursor.fetchall()
# print(rowAll)   #list of tuple

rows = cursor.fetchall()
print(type(rows))
print(rows)
sum = 0
for row in rows:
    sum = sum + row[2]
print(sum)

query = "update customerInfo set Location = %s where CourseName = %s"
data = ("UK","Jmeter")
cursor.execute(query,data)
conn.commit()

# delete

query1 = "delete from customerInfo where courseName = %s"
data1 = ("WebServices",)
cursor.execute(query1,data1)
conn.commit()

conn.close()
