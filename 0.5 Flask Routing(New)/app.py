from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
	return('''
		<html>
		<h1>Hello</h1>
		<h2>welcome to the photo gallerty</h2>
		<p><a href = "/food1">go to first food photo</a></p>
		<p><a href = "/space1">go to first space photo</a></p>
		<p><a href = "/pet2">go to second pet photo</a></p>
		</html>
		 ''')
@app.route('/food1')
def food1():
	return('''
		<html>
		<h1>First photo</h1>
		<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMtt3aOrfYZ1KnQq4GK0vf9gkNBC07f72UWQ&s">
		<h2><a href = "/food2">go to second food picture</h2>
		<h2><a href="/home">go home</a></h2>
		</html>
		 ''')
@app.route('/food2')
def food2():
	return('''
		<html>
		<h1>Second photo</h1>
		<img src="https://images.immediate.co.uk/production/volatile/sites/30/2023/06/Ultraprocessed-food-58d54c3.jpg?quality=90&resize=440,400">
		<h2><a href = "/food3">go to third food picture</a></h2>
		<h2><a href="/food1">go to first photo</a></h2>
		</html>
		 ''')
@app.route('/food3')	
def food3():
	return('''
		<html>
		<h1>Third photo</h1>
		<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTx2qcKAz_hqMRda9TnCrnA1uZEmbAc6vLVQA&s">
		<h2><a href="/home">go home</a></h2>
		<h2><a href = "/food2">go to second food picture</h2>
		</html>
		 ''')


@app.route('/space1')
def space1():
	return('''
		<html>
		<h1>First photo</h1>
		<img src="https://c02.purpledshub.com/uploads/sites/48/2020/04/Things-never-knew-astronomy-e454e5d.jpg">
		<h2><a href = "/space3">go to third space picture</h2>
		<h2><a href="/space2">go to second space picture</h2>
		<h2><a href="/home">go home</a></h2>
		</html>
		 ''')
@app.route('/space2')
def space2():
	return('''
		<html>
		<h1>Second photo</h1>
		<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ5PIw5sl9ZNuo4iEnGXnkvGjKlDHHsjMi8pg&s">
		<h2><a href = "/space3">go to third space picture</a></h2>
		<h2><a href="/space1">go to first photo</a></h2>
		</html>
		 ''')
@app.route('/space3')	
def space3():
	return('''
		<html>
		<h1>Third photo</h1>
		<img src="https://img.freepik.com/free-photo/ultra-detailed-nebula-abstract-wallpaper-4_1562-749.jpg">
		<h2><a href="/space2">go to second space picture</h2>
		<h2><a href = "/space1">go to first space picture</h2>
		</html>
		 ''')

@app.route('/pet1')
def pet1():
	return('''
		<html>
		<h1>First photo</h1>
		<img src="https://www.lonetreevet.com/blog/wp-content/uploads/2017/02/LoneTree_iStock-106396236.jpg">
		<h2><a href="/pet2">go to second pet picture</h2>
		</html>
		 ''')
@app.route('/pet2')
def pet2():
	return('''
		<html>
		<h1>Second photo</h1>
		<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS27yTB-aObq20oZEqdeVtbrs5NQfilNWzFLA&s">
		<h2><a href = "/pet3">go to third pet picture</a></h2>
		<h2><a href="/pet1">go to first pet photo</a></h2>
		<h2><a href="/home">go home</a></h2>
		</html>
		 ''')
@app.route('/pet3')	
def pet3():
	return('''
		<html>
		<h1>Third photo</h1>
		<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYzj1GGPT47pPuFeFZMhOuRRQQfUZ4q-ynzQ&second">
		<h2><a href="/pet2">go to second pet picture</h2>
		</html>
		 ''')  
if __name__ == '__main__':
    app.run(debug=True)