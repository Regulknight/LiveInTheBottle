from bottle import route, run, static_file, post, request
import random

@route('/hello')
def hello():
    return "Hello World!"


@route('/leonid')
def leonnash():
    return "Леонид помнит сюжет не написанных книг"


@route('/login')
def login():
    return static_file("login.html", ".")


@post('/login')
def do_login():
    username = request.forms.get('login')
    password = request.forms.get('password')
    r = random.randint(0, 10)
    if r == 5:
        return "Login Success"
    else:
        return "Login Fail"


run(host='192.168.43.196', port=8080, debug=True)
