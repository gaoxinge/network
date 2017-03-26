#coding=utf-8
import re
from flask import Flask, render_template, url_for, redirect, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a very secret string'

@app.route('/')
@app.route('/<int:num>')
@app.route('/<int:num>s')
def index(num=671):
    return render_template('index.html', num=num)
            
@app.route('/<int:num>m')
def minutes(num):
    return redirect(url_for('index', num=num*60))
    
@app.route('/<int:num>h')
def hours(num):
    return redirect(url_for('index', num=num*3600))
    
@app.route('/custom', methods=['GET', 'POST'])
def custom():
    time = request.form.get('time', 180)
    m = re.match('\d+[smh]?$', time)
    if m is None:
        flash(u'请输入一个有效的时间，例如34、20s、15m、2h')
        return redirect(url_for('index'))
    if time[-1] not in 'smh':
        return redirect(url_for('index', num=int(time)))
    else:
        unit = {'s': 'index', 'm': 'minutes', 'h': 'hours'}
        return redirect(url_for(unit[time[-1]], num=int(time[:-1])))
    
@app.errorhandler(404)
def page_not_found(e):
    flash(u'访问地址出错了，鼠标放在问号上了解更多:)')
    return redirect(url_for('index', num=244))

if __name__ == '__main__':
    app.run()