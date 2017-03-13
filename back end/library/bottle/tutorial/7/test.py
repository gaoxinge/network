#coding=utf-8
from bottle import route, response, run

@route('/wiki')
def wiki():
    response.set_header('Conten-Language', 'en')
    response.set_header('Set-Cookie', 'name=value')
    response.add_header('Set-Cookie', 'name2=value2')
    return u'你好，世界！'
    
run(host='localhost', port=8000)