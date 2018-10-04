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
	itemId		= 0
	request		= ""
	delivery	= ""
	gallons 	= 0
	rate 		= 0
	total		= 0

history1 = client_history()
history2 = client_history()
history3 = client_history()

history1.itemId		= 54321
history1.request 	= "09/18/2018"
history1.delivery 	= "09/20/2018"
history1.gallons 	= 100
history1.rate 		= 2.55
history1.total		= 255

history2.itemId		= 12435
history2.request 	= "09/20/2018"
history2.delivery 	= "09/21/2018"
history2.gallons 	= 123
history2.rate 		= 2.55
history2.total		= 300

history3.itemId		= 52321
history3.request 	= "09/21/2018"
history3.delivery 	= "09/21/2018"
history3.gallons 	= 50
history3.rate 		= 2.55
history3.total		= 12

@app.route("/")
@app.route("/home")
def hello():
	print ('routing . . . home')
	return render_template('home.html')

@app.route("/client_info")
def client_info():
	print ('routing . . . client_info')
	return render_template('client_info.html', client1 = client1)

@app.route("/quote_history")
def quote_history():
	print ('routing . . . quote_history')
	return render_template('quote_history.html', history1 = history1, history2 = history2, history3 = history3)

@app.route("/testpage")
def testpage():
	print ('routing . . . testpage')
	return render_template('testpage.html', client1 = client1, history1 = history1)



if __name__ == '__main__':
	app.run(debug=True)





