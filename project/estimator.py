from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import yaml
import json

app = Flask(__name__)

#configure databse
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)


@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        #fetch form data
        quoteDetails = request.form
        clientId = quoteDetails['client']
        gallons = quoteDetails['gallons']
        reqDate = quoteDetails['reqDate']
        date = quoteDetails['date']
        addr = quoteDetails['address']
        city = quoteDetails['city']
        state = quoteDetails['state']
        _zip = quoteDetails['zip']
        name = quoteDetails['name']
        phone = quoteDetails['phone']
        email = quoteDetails['email']
        rate = quoteDetails['rate']
        total = quoteDetails['total']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO fuelQuote(clientId, gallonsRequested, requestDate, deliveryDate, deliveryAddress, deliveryCity, deliveryState,"
                    " deliveryZipCode, deliveryContactName, deliveryContactPhone, deliveryContactEmail, suggestedPrice, totalAmountDue)"
                    " VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (clientId, gallons, reqDate, date, addr, city, state, _zip, name, phone, email, rate, total))
        mysql.connection.commit()
        cur.close()
        return 'success'
    print ('routing . . . home')
    return render_template('home.html')

@app.route("/client_info")
def client_info():
    print ('routing . . . client_info')
    return render_template('client_info.html')

@app.route("/quote_history")
def quote_history():
    cur = mysql.connection.cursor()
    resetValue = cur.execute("SELECT * FROM fuelQuote")
    if resetValue > 0:
        userDetails = cur.fetchall()
        return render_template('quote_history.html')

    print ('routing . . . quote_history')
    return render_template('quote_history.html')


@app.route("/testpage")
def testpage():
	print ('routing . . . testpage')
	return render_template('testpage.html')



if __name__ == '__main__':
	app.run(debug=True)





