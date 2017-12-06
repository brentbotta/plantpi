#this is a program written by Brent Botta to use a Raspberry Pi to monitor
#indoor plants for temp, humidity and moisture.   12/5/2017
#

#MySQLdb connection string
import mysql.connector

cnx = mysql.connector.connect(user='pi', password='#Bl0nd13007',
                              host='127.0.0.1',
                              database='plantpi')
cursor = cnx.cursor()

#MySQLdb insert record
for x in range(0, 5):
    add_temp = ("INSERT INTO temp (degree) VALUES (%s)") % x
    cursor.execute(add_temp)
    cnx.commit()

#MySQLdb print total row count
cursor.execute ("SELECT COUNT(*) FROM temp")
total_records = cursor.fetchone()
print total_records[0]

#MySQLdb connection close
cursor.close()
cnx.close()