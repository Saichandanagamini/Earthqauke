import csv
import pyodbc
import mysql.connector

# Connect to the MySQL database
server = "tcp:my-server01.database.windows.net"
database = "My-db"
username = "sxg6912"
password = "PoiuytrewQ@239"
driver = "{ODBC Driver 18 for SQL Server}"

#account_name = "assign1"
#account_key = "LRQ7KMFLfj76yCbLIdfF0VeLYyrNvkTWPi35Xt6vumz/XmL74jiUCeTzvSahTMKVTrN/N5AwqXm9+AStsZurlQ=="
#container_name = "assgn_pics"

#cnxn = mysql.connector.connect(user='sxg6912', password='PoiuytrewQ@239',
 #                             host='localhost',
  #                            database='My-db')

cnxn = pyodbc.connect('DRIVER='+ driver + ';SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
# Create a cursor object to execute SQL queries
cursor = cnxn.cursor()

# Open the CSV file and read the data
with open('earthquake_month.csv', 'r') as f:
    reader = csv.reader(f)
    #print(reader)
    next(reader) # skip the header row
    i = 1
    for row in reader:
        # Insert the data into the earthquakes table
        #print(row)
        #print(row[0])
        #cursor.execute("INSERT INTO earthquakes VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21]))
        print("INSERT INTO earthquakes VALUES (" + str(i) + "," + row[23] + "," + row[2] + "," + row[3] + "," + row[
            4] + "," + row[5] + "," + "'" + row[6] + "'" + "," + str(int(float(row[7]))) + "," + row[8] + "," + row[
                  9] + "," + row[10] + "," + "'" + row[11] + "'" + "," + "'" + row[20] + "'" + "," + "'" + row[
                  21] + "'" + "," + "'" + row[22] + "'" + ")")
        cursor.execute("INSERT INTO earthquakes VALUES ("+ str(i) + "," + row[23] + "," + row[2] + "," + row[3] + "," + row[4] + "," + row[5] + ","  + "'" + row[6] + "'" + "," + str(int(float(row[7]))) + "," + row[8] + "," + row[9] + "," + row[10] + "," + "'" + row[11] + "'" + "," + "'" + row[20] + "'" + "," + "'" + row[21] + "'" + "," + "'" + row[22] + "'" + ")")
        #print(int(float(row[7])))

        i = i + 1
        #print("INSERT INTO earthquakes VALUES (" + "'" + row[0] + "'" + "," + "'" + row[1] + "'" + "," + "'" + row[2] + "'" + "," + "'" + row[3] + "'" + "," + "'" + row[4] + "'" + "," + "'" + row[5] + "'" + "," + "'" + row[6] + "'" + "," + "'" + row[7] + "'" + "," + "'" + row[8] + "'" + "," + "'" + row[9] + "'" + "," + "'" + row[10] + "'" + "," + "'" + row[11] + "'" + "," + "'" + row[12] + "'" + "," + "'" + row[13] + "'" + "," + "'" + row[14] + "'" + "," + "'" + row[15] + "'" + "," + "'" + row[16] + "'" + "," + "'" + row[17] + "'" + "," + "'" + row[18] + "'" + "," + "'" + row[19] + "'" + "," + "'" + row[20] + "'" + "," + "'" + row[21] + "'" + ")")


        #print("INSERT INTO earthquakes VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", tuple(row))
        #cursor.execute("INSERT INTO earthquakes VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", tuple(row))

# Commit the changes to the database
cnxn.commit()

# Close the cursor and database connection
cursor.close()
cnxn.close()