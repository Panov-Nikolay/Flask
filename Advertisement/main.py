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

@app.route('/promotion_image')
def bootstrap():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.jpg')}" 
                        alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-dark" role="alert">
                      <h3>Человечество вырастает из детства.</h3>
                    </div>
                    <div class="alert alert-success" role="alert">
                      <h3>Человечеству мала одна планета.</h3>
                    </div>
                    <div class="alert alert-dark" role="alert">
                      <h3>Мы сделаем обытаемыми безжизненные пока планеты.</h3>
                    </div>
                    <div class="alert alert-warning" role="alert">
                      <h3>И начнем с Марса!</h3>
                    </div>
                    <div class="alert alert-danger" role="alert">
                      <h3>Присоединяйся!</h3>
                    </div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')