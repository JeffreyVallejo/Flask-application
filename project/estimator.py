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



@app.route("/")
@app.route("/home")
def hello():
	return render_template('home.html')

@app.route("/client_info")
def client_info():
	return render_template('client_info.html', client1 = client1)

@app.route("/testpage")
def testpage():
	return render_template('testpage.html', client1 = client1)



if __name__ == '__main__':
	app.run(debug=True)





