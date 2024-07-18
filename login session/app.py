from flask import Flask, render_template,url_for,redirect,request, session
import random



app = Flask(__name__,template_folder="templates",static_folder="static")
app.config['SECRET_KEY'] = "Amir"
fortunes = ["Amir will be your TA(Good)","Amir will not be your TA(Bad)","Paulina will be your Ta(decent)","Paulina will not be your TA(not ideal)",
"you wont get double CS(inshallah)","You will get double CS(wallah you should run)","Y1's will take the fusball table","Y1 will go back(Amazing)"]
@app.route('/', methods = ['GET','POST'])
def home():
	if request.method == 'GET':
		return redirect(url_for("login"))
	else:
		session['birthday'] = request.form['birthday']
		session['name']=request.form['name']
		return render_template('home.html')

@app.route('/login')
def login():
		return render_template("login.html")

@app.route('/fortune', methods = ['GET','POST'])
def fortune():
	if len(session['birthday']) > 7:
		fort = fortunes[4]
	else:
		fort = fortunes[len(session['birthday'])]
	return render_template("fortune.html",fort = fort)


if __name__ == '__main__':
    app.run(debug=True)