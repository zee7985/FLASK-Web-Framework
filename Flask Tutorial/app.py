from flask import Flask

#__name__ == __main__
app =Flask(__name__)  #object creation

#Routes-for user to goto different url
@app.route('/') #when user come at this url hello function(below) will be trigerred
def hello():
	return "Hello World"


if __name__=='__main__':
	app.debug=True     # so that we donot need to restart the server after making changes
	app.run()