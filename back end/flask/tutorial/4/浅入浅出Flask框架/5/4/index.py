from flask import Flask, url_for
from werkzeug.routing import BaseConverter

class MyIntConverter(BaseConverter):
    
    def __init__(self, url_map):
        super(MyIntConverter, self).__init__(url_map)
        
    def to_python(self, value):
        return int(value)
        
    def to_url(self, value):
        return 'hi'
        
app = Flask(__name__)
app.url_map.converters['my_int'] = MyIntConverter

@app.route('/')
def hello_world():
    return 'hello world'
    
@app.route('/page/<my_int:num>')
def page(num):
    print num
    print url_for('page', num='123')
    return 'hello world'
    
if __name__ == '__main__':
    app.run(debug=True)