from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/home')
def home():
    return render_template('/home.html')


@app.route('/menu')
def menu():
    return render_template('menu.html')


@app.route('/add_flower')
def add_flower():
    return render_template('add_flower.html')


@app.route('/del_flower')
def del_flower():
    return render_template('del_flower.html')


@app.route('/records')
def records():
    return render_template('records.html')


@app.route('/order')
def order():
    return render_template('order.html')


@app.route('/last')
def last():
    return render_template('last.html')


if __name__ == "__main__":  # for triggering the project...
    app.run(debug=True)
