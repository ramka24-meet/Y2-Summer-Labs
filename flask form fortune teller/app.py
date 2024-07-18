from flask import Flask, render_template,url_for,redirect,request
import random



app = Flask(__name__,template_folder="templates",static_folder="static")
fortunes = ["Amir will be your TA(Good)","Amir will not be your TA(Bad)","Paulina will be your Ta(decent)","Paulina will not be your TA(not ideal)",
"you wont get double CS(inshallah)","You will get double CS(wallah you should run)","Y1's will take the fusball table","Y1 will go back(Amazing)"]
@app.route('/', methods = ['GET','POST'])
def home():
	if request.method == 'GET':
		return render_template("home.html")
	else:
		birthday = request.form['birthday']
		return redirect(url_for('fortune', birthday = birthday))


@app.route('/fortune/<birthday>', methods = ['GET','POST'])
def fortune(birthday):
	if len(birthday) > 7:
		fort = fortunes[4]
	else:
		fort = fortunes[len(birthday)]
	return render_template("fortune.html",fort = fort)


if __name__ == '__main__':
    app.run(debug=True)