from flask import Flask, render_template,url_for,redirect,request, session 
import pyrebase
config = {

  "apiKey": "AIzaSyCgCJr5z24r8Hq1OF-EaHPSyIpR_NAEqcg",

  "authDomain": "auth-lab-f25dd.firebaseapp.com",

  "projectId": "auth-lab-f25dd",

  "storageBucket": "auth-lab-f25dd.appspot.com",

  "messagingSenderId": "962415959144",

  "appId": "1:962415959144:web:c25931fa288a359c002fdd",

  "databaseURL":""

}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = "Amir"

@app.route('/', methods = ['GET', 'POST'])
def signUp():
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		try:
			session['user'] = auth.create_user_with_email_and_password(email, password)
			session['quotes'] = None
			return redirect(url_for('home'))
		except:
			error = "Authentication failed"
	return render_template("signup.html")


@app.route('/sign-in')
def signIn():
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		try:
			login_session['user'] = auth.sign_in_with_email_and_password(email, password)
			return redirect(url_for('home'))
		except:
			error = "Authentication failed"
	return render_template("signin.html")

@app.route('/display')
def display():
	pass
@app.route('/thanks')
def thanks():
	pass


if __name__ == '__main__':
    app.run(debug=True)