from flask import Flask,render_template,redirect
#render_template - to use html file 

app =Flask(__name__)  

#Flask uses Ginger template to write python code in html
friends=["ABC","DEF","XYZ"]
num=5

@app.route('/') 
def hello():
	return render_template("index.html",my_friends=friends,number=num)  #pass our friends list to html 

@app.route('/about') 
def about():
	return "<h1> About Page</h1>"  #either we can write whole html here or use render

@app.route('/home') 
def home():
	return redirect('/')

if __name__=='__main__':
	app.debug=True     
	app.run()