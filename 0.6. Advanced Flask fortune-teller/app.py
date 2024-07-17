from flask import Flask, render_template
import random


fortunes = ["Amir will be your TA(Good)","Amir will not be your TA(Bad)","Paulina will be your Ta(decent)","Paulina will not be your TA(not ideal)",
"you wont get double CS(inshallah)","You will get double CS(wallah you should run)","Y1's will take the fusball table","Y1 will go back(Amazing)"]
app = Flask(__name__,template_folder="templates",static_folder="static")
fortuness =random.choice(fortunes)
@app.route('/')
def home():
	return render_template("home.html")
@app.route('/fortune')
def fortune():
	return render_template("fortune.html",fort = fortuness)
if __name__ == '__main__':
    app.run(debug=True)