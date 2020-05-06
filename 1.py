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

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')