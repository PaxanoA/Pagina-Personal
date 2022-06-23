from flask import Flask, render_template

app = Flask(__name__) #initialize app


#create Rutes @app.route('routeName')
@app.route('/')#home/Andres Pachano
def index():
	return render_template('home.html')

@app.route('/about-me')
def AP():
	return render_template('about-me.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/curriculum-vitae')
def CV():
	return render_template('##insertarLinkGoogleDrive')

#LISTENER
if __name__ == '__main__':
	app.run(debug=True)