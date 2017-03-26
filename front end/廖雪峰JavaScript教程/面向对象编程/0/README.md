```javascript
// xiaoming ---> Object.prototype ---> null
var xiaoming = new Object({name: '小明'});
```

```javascript
// xiaoming ---> Student ---> Object.prototype ---> null
var Student = new Object({name: 'Robot', height: 1.2, run: function(){console.log(this.name + ' is runnint...');}});
xiaoming.__proto__ = Student;
```