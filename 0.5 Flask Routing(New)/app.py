from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
	return('''
		<html>
		<h1>Hello</h1>
		<h2>welcome to the photo gallerty</h2>
		<p><a href = "/food1">go to fisrt photo</a></p>
		</html>
		 ''')
@app.route('/food1')
def home():
	return('''
		<html><h1>First photo</h1></html>
		 ''')

    
if __name__ == '__main__':
    app.run(debug=True)