from flask import Flask, render_template, request
import pyodbc
import mysql.connector

app = Flask(__name__)

# Define the database connection details
server = "tcp:my-server01.database.windows.net"
database = "My-db"
username = "sxg6912"
password = "PoiuytrewQ@239"
driver = "{ODBC Driver 17 for SQL Server}"

@app.route('/')
def home():
    return render_template("Home.html")

@app.route('/', methods=['POST'])
def my_form():
    query = request.form['5mag']
    cnxn = pyodbc.connect(
        'DRIVER=' + driver + ';SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    print(query)
    cursor = cnxn.cursor()
    cursor.execute(query)
    row = cursor.fetchall()
    data = []
    for i in range(len(row)):
        l = list(row[i])
        print(l)
        data.append(l)

    return get_data(data)


@app.route('/mag5')
def get_data(data):
    return render_template("earthquakesmag.html", data=data)



app.run()

# Define a route to handle the home page
#@app.route('/')
#def home():
#    return render_template('home.html')

# Define a route to handle queries for earthquakes with a magnitude greater than 5.0
#@app.route('/mag_gt_5')
#def mag_gt_5():
#    cnxn = pyodbc.connect(
#        'DRIVER=' + driver + ';SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
#    cursor = cnxn.cursor()
#    cursor.execute(f"SELECT * FROM [dbo].[earthquake_month] WHERE mag > 5")
#    row = cursor.fetchall()
#    print(row)
 #   for i in range(len(row)):

#    return get_earthquakemag()

#def get_earthquakemag():
#    return render_template('earthquakesmag.html')
