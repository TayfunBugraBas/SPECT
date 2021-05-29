from flask import Flask, render_template, request , jsonify
from flask_mysqldb import MySQL
from mysql import connector
import mysql.connector

app = Flask(__name__)


app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "1234"
app.config['MYSQL_DB'] ="flaskapp"

mysql1 = MySQL(app)

@app.route('/', methods=['GET','POST'])
def index():

	return render_template("index.html")

@app.route('/database')
def users():
	cur = mysql1.connection.cursor()
	resultValue = cur.execute("SELECT * FROM new_table")
	if resultValue > 0:
		spectDetails = cur.fetchall()
		return render_template('database.html',spectDetails = spectDetails)

@app.route('/VeriDatabase')
def users2():
	curs = mysql1.connection.cursor()
	resultValue2 = curs.execute("SELECT * FROM hepsisonuclu")
	if resultValue2 > 0:
		spectDetails = curs.fetchall()
		return render_template('VeriDatabase.html',spectDetails = spectDetails)

@app.route('/Features')
def users3():
	curs = mysql1.connection.cursor()
	resultValue2 = curs.execute("SELECT * FROM featuresselection")
	if resultValue2 > 0:
		spectDetails = curs.fetchall()
		return render_template('Features.html',spectDetails = spectDetails)
  
@app.route('/Search')
def search():  

	return render_template("SearchinDatabase.html")

@app.route('/Result',methods=['POST','GET'])
def result():
   mydb = mysql.connector.connect(
	   host="localhost",
	   user="root",
	   password="1234",
	   database="flaskapp"
   )

   mycursora=mydb.cursor()
   if request.method=='POST':
	   result=request.form

	   name=result['Name']

	   mycursora.execute("select ClassificationNames,Trues,Falses,Accuracy from new_table where ClassificationNames='"+name+"'")

	   r=mycursora.fetchone()

	   mydb.commit()
	   mycursora.close()

	   return render_template("response.html",r=r)


if __name__ == "__main__":
	app.run(debug=True)