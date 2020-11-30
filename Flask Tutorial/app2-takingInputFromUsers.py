from flask import Flask,render_template,redirect,request
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

@app.route('/home')  #here we haven't use get or post because bty default it is get
def home():
	return redirect('/')

@app.route('/submit',methods=['POST']) 
def submit():
	if request.method =='POST':
		name=request.form['username']  #request.form is a dict {username:"the name we have given(eg-ABC) "}

		f=request.files['userfile']  #samething we will do for file use dict

		f.save(f.filename)    #It will save the file in our current directory with the same file name
	return "<h1> Hello{}".format(name)

if __name__=='__main__':
	app.debug=True     
	app.run()