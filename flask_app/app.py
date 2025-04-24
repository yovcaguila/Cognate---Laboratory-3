from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        return render_template('thankyou.html', name=name, message=message)
    return render_template('contact.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
