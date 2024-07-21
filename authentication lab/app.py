from flask import Flask, render_template,url_for,redirect,request, session 
import pyrebase
Config = {

  "apiKey": "AIzaSyCgCJr5z24r8Hq1OF-EaHPSyIpR_NAEqcg",

  "authDomain": "auth-lab-f25dd.firebaseapp.com",

  "projectId": "auth-lab-f25dd",

  "storageBucket": "auth-lab-f25dd.appspot.com",

  "messagingSenderId": "962415959144",

  "appId": "1:962415959144:web:c25931fa288a359c002fdd",

  "databaseURL":""

}

firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = "Amir"

@app.route('/', methods = ['GET', 'POST'])
def signUp():
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		try:
			print("hello")
			session['user'] = auth.create_user_with_email_and_password(email, password)
			session['quote'] = ""
			session['quotes'] = []
			return redirect(url_for('home'))
		except:
			error = "Authentication failed"
	return render_template("signup.html")


@app.route('/sign-in', methods=['GET','POST'])
def signIn():
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		try:
			session['user'] = auth.sign_in_with_email_and_password(email, password)
			session['quote'] = ""
			session['quotes'] = []
			return redirect(url_for('home'))
		except:
			error = "Authentication failed"
	return render_template("signin.html")
@app.route('/home', methods = ['GET','POST'])
def home():
	if request.method == 'POST':
		print(session['quote'])
		quote = request.form['quote']
		session['quote'] = quote
		return redirect(url_for('thanks'))
	return render_template('home.html')
@app.route('/display')
def display():
	quotes = session['quotes']
	print(session['quotes'])
	return render_template("display.html", quotes = quotes)
@app.route('/thanks')
def thanks():
	quote = session['quote']
	session['quotes'].append(quote)
	session.modified = True
	print(session['quotes'])
	return render_template("thanks.html",quote = quote)
@app.route('/sign-out')
def signOut():
	session['user']=None
	auth.current_user = None
	return redirect(url_for('signIn'))

if __name__ == '__main__':
    app.run(debug=True)