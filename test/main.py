from bottle import route, run


@route('/hello')
def hello():
    return "Hello World!"


@route('/leonid')
def leonnash():
    return "Леонид помнит сюжет не написанных книг"

run(host='localhost', port=8080, debug=True)