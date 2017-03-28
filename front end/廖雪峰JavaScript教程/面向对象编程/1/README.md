```javascript
/*
 * Student  ---> Function.prototype ---> Object.prototype ---> null
 * xiaoming ---> Student.prototype  ---> Object.prototype ---> null
 */
var Student = new Function('name', 'this.name=name;this.hello=function(){return \'Hello, \' + this.name + \'!\';}');
var xiaoming = new Student('小明');
```