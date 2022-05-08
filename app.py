from flask import Flask, render_template, request , url_for

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home_page.html')


@app.route('/aeroponics')
def aeroponics():
    return render_template('aeroponics.html')

@app.route('/hydroponics')
def hydroponics():
    return render_template('Hydroponics.html')



if __name__ == '__main__':
	app.run(debug=True)