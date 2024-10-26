import mysql.connector

dataConnection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'ex@mvibgyor2025',
        database = 'climate'
    )
cursor = dataConnection.cursor()
#cursor.execute("CREATE DATABASE climate")
cursor.execute("CREATE TABLE weather( \
            date VARCHAR(2), \
            air_temp_min FLOAT(3,2), \
            air_temp_avg FLOAT(3,2), \
            air_temp_max FLOAT(3,2), \
            air_temp_depar_normal DECIMAL(2, 1), \
            precipitation FLOAT(3,1))")
dataConnection.commit()
cursor.close()
dataConnection.close()
