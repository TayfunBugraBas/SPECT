from flask import Flask, render_template, request , jsonify
from flask_mysqldb import MySQL,MySQLdb
import mysql.connector as mysql

app = Flask(__name__)


app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "1234"
app.config['MYSQL_DB'] ="flaskapp"
mysql = MySQL(app)

@app.route('/', methods=['GET','POST'])
def index():

	return render_template("index.html")

@app.route('/database')
def users():
	cur = mysql.connection.cursor()
	resultValue = cur.execute("SELECT * FROM new_table")
	if resultValue > 0:
		spectDetails = cur.fetchall()
		return render_template('database.html',spectDetails = spectDetails)

@app.route('/VeriDatabase')
def users2():
	curs = mysql.connection.cursor()
	resultValue2 = curs.execute("SELECT * FROM hepsisonuclu")
	if resultValue2 > 0:
		spectDetails = curs.fetchall()
		return render_template('VeriDatabase.html',spectDetails = spectDetails)

@app.route('/Features')
def users3():
	curs = mysql.connection.cursor()
	resultValue2 = curs.execute("SELECT * FROM featuresselection")
	if resultValue2 > 0:
		spectDetails = curs.fetchall()
		return render_template('Features.html',spectDetails = spectDetails)


if __name__ == "__main__":
	app.run(debug=True)