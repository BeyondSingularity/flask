from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/')
def main_page():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Миссия Колонизация Марса</title>
                  </head>
                  <body>
                    <h1>Миссия Колонизация Марса</h1>
                  </body>
                </html>"""


@app.route('/index')
def index():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Миссия Колонизация Марса</title>
                  </head>
                  <body>
                    <h1>И на Марсе будут яблони цвести!</h1>
                  </body>
                </html>"""


@app.route('/promotion')
def promotion():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Миссия Колонизация Марса</title>
                  </head>
                  <body>
                    <h1>Человечество вырастает из детства.<br/><br/>
                    Человечеству мала одна планета.<br/><br/>Мы сделаем обитаемыми безжизненные 
                    пока планеты.<br/><br/>И начнем с Марса!<br/><br/>Присоединяйся!</h1>
                  </body>
                </html>"""


@app.route('/image_mars')
def image_mars():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                    <body>
                      <h1>Жди нас, Марс!</h1>
                      <img src="{}" alt="Утёкшие в сеть реальные фото Марса">
                      <h4>А что вы ждали?</h4>
                   </body>
                 </html>""".format(url_for('static', filename='img/mars_candy.png'))


@app.route('/promotion_image')
def promotion_image():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <link rel="stylesheet" href="https://stackpath.bootstrap
                    cdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x
                    4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                     crossorigin="anonymous">
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                    <body>
                      <h1>Жди нас, Марс!</h1>
                      <img src="{}" alt="Утёкшие в сеть реальные фото Марса">
                      <h4>А что вы ждали?</h4>
                      <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js"
                       integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0
                       wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
                      <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/
                      popper.min.js" integrity="sh
                      a384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo"
                       crossorigin="anonymous"></script>
                      <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bo
                      otstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7Ywa
                      Yd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
                   </body>
                 </html>""".format(url_for('static', filename='img/mars_candy.png'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')