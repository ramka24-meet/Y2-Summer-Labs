from flask import Flask, render_template,url_for,redirect,request, session 
import google.generativeai as genai
import pathlib
import pyrebase
import os


#gemini setup
api_key = 'AIzaSyCnjIEiE-WffSm_ne306QOaK94HTd-bezg'
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')
akinator_chat = model.start_chat(history=[])
gpt_chat = model.start_chat(history=[])

#firebase setup
Config = {
  "apiKey": "AIzaSyAwU4XvjzY3pZT9Iw2Kwyv8pWQwjT3R5fk",
  "authDomain": "gemini-2f479.firebaseapp.com",
  "databaseURL": "https://gemini-2f479-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "gemini-2f479",
  "storageBucket": "gemini-2f479.appspot.com",
  "messagingSenderId": "294253943244",
  "appId": "1:294253943244:web:920aab62c939ba50e06569",
  "databaseURL" : "https://gemini-2f479-default-rtdb.europe-west1.firebasedatabase.app/"
}
firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()
db = firebase.database()
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = "Amir"

#project
@app.route('/', methods = ['GET', 'POST'])
def signUp():
  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']
    username = request.form['username']
    try:
      user = {'email' : email, 'username': username}
      session['user'] = auth.create_user_with_email_and_password(email, password)
      db.child('Users').child(session['user']['localId']).set(user)
      return redirect(url_for('home'))
    except:
      error = "Authentication failed"
      return redirect(url_for("error"))
  return render_template("signup.html")

@app.route('/sign-in', methods=['GET','POST'])
def signIn():
  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']
    try:
      session['user'] = auth.sign_in_with_email_and_password(email, password)
      return redirect(url_for('home'))
    except:
      error = "Authentication failed"
      return redirect(url_for("error"))
  return render_template("signin.html")

@app.route('/home', methods = ['GET', 'POST'])
def home():
  return render_template('home.html')
@app.route('/scribble', methods = ['GET', 'POST'])
def scribble():
  return render_template("scribble.html")

@app.route('/akinator', methods = ['GET', 'POST'])
def akinator():
  if request.method == 'GET':
    response = akinator_chat.send_message("""
You are Akinator, a genius that can guess any character a user is thinking of by asking a series of specific questions.
Your goal is to ask targeted questions that help you identify the character. minimize asking about specific shows or unrelated topics,
and focus only on attributes and traits of the character. Dont be afraid to guess the character without being 100 precent sure
Ask only yes or no questions and do not repeat questions.

Examples of good questions:
1. Is the character real?
2. Is the character human?
3. Is the character male?
4. Is the character from a movie?
5. Does the character have magical powers?


Begin your questioning now:
""")
    return render_template("akinator.html", response = response.text)
  if request.method == 'POST':
    picked_option = request.form.get('akinator')
    response = akinator_chat.send_message(picked_option).text
    if response == 'GUESS':
      return render_template('correct.html')
    return render_template("akinator.html", response = response)
@app.route('/gpt', methods = ['GET', 'POST'])
def gpt():
  return render_template("gpt.html")

@app.route('/profile', methods = ['GET', 'POST'])
def profile():
  return render_template("profile.html")

@app.route('/error',methods = ['GET', 'POST'])
def error():
  return render_template("error.html")
if __name__ == '__main__':
    app.run(debug=True)