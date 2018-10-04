from flask import Flask, render_template
app = Flask(__name__)

# This is where we will add class -> clientInfo
class clientInfo:
	clientId	= 12345
	name     	= "jerry winberg"
	address	 	= "123 life St"
	phone		= "123-456-7890"
	email		= "example@service.com"

#object of type clientInfo
client1 = clientInfo()

class client_history:
	itemId		= 54321
	request		= "09182018"
	delivery	= "09252018"
	gallons 	= 100
	rate 		= 2.55
	total		= 255

history1 = client_history()


@app.route("/")
@app.route("/home")
def hello():
	return render_template('home.html')

@app.route("/client_info")
def client_info():
	return render_template('client_info.html', client1 = client1)

@app.route("/quote_history")
def quote_history():
	return render_template('quote_history.html', history1 = history1)

@app.route("/testpage")
def testpage():
	return render_template('testpage.html', client1 = client1, history1 = history1)



if __name__ == '__main__':
	app.run(debug=True)





