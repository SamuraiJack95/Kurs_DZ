from flask import Flask, render_template, url_for, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = '14fmrmkndek4493lgttmdvk3297dovvm3m56m122mfkfpewotiv34kciw3ew'
menu = [
    {'name': 'Главная', 'url': '/'},
    {'name': 'О нас', 'url': '/about'},
    {'name': 'Контакты', 'url': '/contacts'}
]

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html', title='Главная', menu=menu)

@app.route('/about')
def about():
    return render_template('about.html', title='О нас', menu=menu)

@app.route('/contacts', methods=['POST','GET'])
def contacts():
    if request.method == 'POST':
        if len(request.form['username']) > 1:
            flash('Сообщение отправлено успешно!', category='success')
        else:
            flash('Сообщение не отправлено, ошибка!', category='error')

        print(request.form)
        context = {
            'username': request.form['username'],
            'email': request.form['email'],
            'message': request.form['message']
        }
        return render_template('contacts.html', **context, title='Контакты', menu=menu)
    return render_template('contacts.html', title='Контакты', menu=menu)

@app.route('/profile/<username>')
def profile(username):
    return f'Пользователь{username}'

@app.route(404)
def page_not_found(error):
    return render_template('page404.html', title='Страница не найдена', menu=menu), 404



if __name__ == '__main__':
    app.run(debug=True)
