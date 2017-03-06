from bottle import route, response, run

@route('/iso')
def get_iso():
    response.charset = 'ISO-8859-15' # error: can't set attribute
    return u'This will be sent with ISO-8859-15 encoding'
    
@route('/latin')
def get_latin():
    response.content_type = 'text/html; charset=latin9'
    return u'ISO-8859-15 is also known as latin9'

run(host='localhost', port=8000)