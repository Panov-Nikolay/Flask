from flask import Flask, url_for

app = Flask(__name__)

arr = ['Человечество вырастает из детства.',
       'Человечеству мала одна планета.',
       'Мы сделаем обитаемыми безжизненные пока планеты.',
       'И начнем с Марса!',
       'Присоединяйся!']


@app.route('/image_mars')
def header():
    return f"""<header>Привет, Марс!</header>
            <h1>Жди нас, Марс!</h1>
            <figure>
                <img src="{url_for('static', filename='img/mars.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">
                <figcaption>Вот она какая, красная планета</figcaption>
            </figure>"""

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')