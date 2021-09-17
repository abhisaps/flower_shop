from flask import Flask, render_template, request, url_for
from src1.menu1 import menu1
from src1.add_flower import adding

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/menu')
def menu():
    m = menu1
    return render_template('menu.html', m=menu1)


@app.route('/add_flower')
def add_flower():
    return render_template('add_flower.html')


@app.route('/add_flower', methods=["POST"])
def get_flower():
    f_code = request.form['f_code']
    f_quantity = request.form['f_quantity']
    f_name = request.form['f_name']

    return render_template('pass.html', f_code=f_code, f_quantity=f_quantity, f_name=f_name)


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
