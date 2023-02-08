from flask import Flask, url_for, request


app = Flask(__name__)


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <h2>на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="fname" placeholder="Введите фамилию", name="fname">
                                    <input type="text" class="form-control" id="iname" placeholder="Введите имя", name="iname">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="educationSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="educationSelect" name="education">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <label for="about">Какие у Вас есть профессии?</label>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="инженер-исследователь" id="1">
                                            <lable class="form-check-label">Инженер-исследователь</lable>
                                        </div>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="пилот" id="2">
                                            <lable class="form-check-label">Пилот</lable>
                                        </div>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="строитель" id="3">
                                            <lable class="form-check-label">Cтроитель</lable>
                                        </div>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="экзобиолог" id="4">
                                            <lable class="form-check-label">Экзобиолог</lable>
                                        </div>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="врач" id="5">
                                            <lable class="form-check-label">Врач</lable>
                                        </div>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="инженер по терраформированию" id="6">
                                            <lable class="form-check-label">Инженер по терраформированию</lable>
                                        </div>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="климатолог" id="7">
                                            <lable class="form-check-label">Климатолог</lable>
                                        </div>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="специалист по радиационной защите" id="8">
                                            <lable class="form-check-label">Специалист по радиационной защите</lable>
                                        </div>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="астрогеолог" id="9">
                                            <lable class="form-check-label">Астрогеолог</lable>
                                        </div>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="гляциолог" id="10">
                                            <lable class="form-check-label">Гляциолог</lable>
                                        </div>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="инженер жизнеобеспечения" id="11">
                                            <lable class="form-check-label">Инженер жизнеобеспечения</lable>
                                        </div>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="метеоролог" id="12">
                                            <lable class="form-check-label">Метеоролог</lable>
                                        </div>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="оператор марсохода" id="13">
                                            <lable class="form-check-label">Оператор марсохода</lable>
                                        </div>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="киберинженер" id="14">
                                            <lable class="form-check-label">Киберинженер</lable>
                                        </div>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="штурман" id="15">
                                            <lable class="form-check-label">Штурман</lable>
                                        </div>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="пилот дронов" id="16">
                                            <lable class="form-check-label">Пилот дронов</lable>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['fname'])
        print(request.form['iname'])
        print(request.form['email'])
        print(request.form['education'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['sex'])
        print(request.form['accept'])
        return "Форма отправлена"
    
    
if __name__ == '__main__':
    app.run(port=8081, host='127.0.0.1')