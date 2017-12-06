import mysql.connector

cnx = mysql.connector.connect(user='pi', password='#Bl0nd13007',
                              host='127.0.0.1',
                              database='plantpi')
cursor = cnx.cursor()
#Need to update the values below and support autonumbering
add_temp = ("INSERT INTO temp (idtemp, temp) VALUES (2,13)")
cursor.execute(add_temp)
cnx.commit()
cursor.close()
cnx.close()