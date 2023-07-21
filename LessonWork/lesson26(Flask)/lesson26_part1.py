from flask import Flask, render_template, request

app = Flask(__name__)

menu = [
    {'name': 'Главная', 'url': '/'},
    {'name': 'О сайте', 'url': 'about'},
    {'name': 'Обратная связь', 'url': 'contacts'}
]


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html', title='Главная', menu=menu)


@app.route('/about')
def about():
    return render_template('about.html', menu=menu)


@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    if request.method == 'POST':
        return render_template('index.html', title='Главная', menu=menu)
    return render_template('contacts.html', title='Обратная связь', menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
