from bottle import route, static_file, run

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='.')

run(host='localhost', port=8000)