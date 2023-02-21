from flask import Flask, render_template
from werkzeug.utils import redirect
from loginform import LoginForm
from data import db_session
from data.users import User
import datetime
from data.news import News

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    user = "Ученик Яндекс.Лицея"
    return render_template('index.html', title='Домашняя страница',
                           username=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/success')
def odd_even():
    return "УРАААААААА!!!!!!"


def create_users():
    for i in range(1, 101):
        user = User()
        user.name = f"Пользователь {i}"
        user.about = f"биография пользователя {i}"
        user.email = f"email{i}@email.ru"
        db_sess.add(user)
    db_sess.commit()

if __name__ == '__main__':
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id == 1).first()
    for news in user.news:
        print(news)
    # app.run(port=8080, host='127.0.0.1')