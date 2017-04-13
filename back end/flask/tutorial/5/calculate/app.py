#-*- coding:utf-8 -*-
from flask import Flask, jsonify, request, render_template, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        result = eval(request.form.get('expression'))
    except Exception, e:
        result =  str(e)
    return jsonify(result=result)
    
if __name__ == '__main__':
    app.run()