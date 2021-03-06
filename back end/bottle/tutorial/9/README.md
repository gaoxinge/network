# SimpleTemplate Engine

```python
>>> from bottle import SimpleTemplate, template
>>> tp1 = SimpleTemplate('Hello {{name}}!') # compile
>>> tp1.render(name='World')                # render
u'Hello World!'
template('Hello {{name}}!', name='World')
u'Hello World!'
```

```python
>>> mydict = {'number': '123', 'street': 'Fake St.', 'city': 'Fackville'}
>>> template('I like at {{number}} {{street}}, {{city}}', mydict)
u'I like at 123 Fake St., Fackville'
>>> template('I like at {{number}} {{street}}, {{city}}', **mydict)
u'I like at 123 Fake St., Fackville'
```

```python
>>> template('Hello {{name.title() if name else "stranger"}}', name=None)
u'Hello stranger'
>>> template('Hello {{name.title() if name else "stranger"}}', name='mArc')
u'Hello Marc'
```

```python
>>> template('<ul>\n%for item in [1,2,3]:\n<li>{{item}}</li></ul>')
u'<ul>\n<li>1</li></ul><li>2</li></ul><li>3</li></ul>'
>>> template('<ul>\n%a=1\n</ul>{{a}}')
u'<ul>\n</ul>1'
>>> template('<ul>\n%a=1\n</ul>%a\n<p></p>')
u'<ul>\n</ul>%a\n<p></p>'
>>> template('<ul>\n%a=1\n</ul>%print 1')
u'<ul>\n</ul>%print 1'
>>> template('<ul>\n%a=1\n</ul>%print {{a}}')
u'<ul>\n</ul>%print 1'
>>> template('<ul>\n%a=1\n</ul>%print a')
u'<ul>\n</ul>%print a'
```