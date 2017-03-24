# 面向对象编程

## 原型链

- 原型链的作用是为了对象查找属性。它是由函数对象的prototype，__proto__，constructor和普通对象的__proto__，constructor维系的

def f() {}     ---> Function.prototype ---> Object.prototype ---> null

1              ---> Number.prototype   ---> Object.prototype ---> null

new Number(1)  ---> Number.prototype   ---> Object.prototype ---> null

true           ---> Boolean.prototype  ---> Object.prototype ---> null

new Boolean(1) ---> Boolean.prototype  ---> Object.prototype ---> null

'1'            ---> String.prototype   ---> Object.prototype ---> null

new String(1)  ---> String.prototype   ---> Object.prototype ---> null

[]             ---> Array.prototype    ---> Object.prototype ---> null

{}             ---> Object.prototype   ---> null

Math           ---> Object.prototype   ---> null

JSON           ---> Object.prototype   ---> null

## 特殊方法（魔术方法）

- __defineGetter__
- __defineSetter__
- __lookupGetter__
- __lookupSetter__
- __proto__
- constructor
- hasOwnProperty
- isPropertyOf
- propertyIsEnumerable
- toLocaleString
- toString
- valueOf
- prototype（函数对象）

## typeof和instanceof

- [typeof](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/typeof)
- [instanceof](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/instanceof)

## 参考

- [最详尽的JS原型与原型链终极详解，没有「可能是」。（一）](http://www.jianshu.com/p/dee9f8b14771)
- [最详尽的JS原型与原型链终极详解，没有「可能是」。（二）](http://www.jianshu.com/p/652991a67186)
- [最详尽的JS原型与原型链终极详解，没有「可能是」。（三）](http://www.jianshu.com/p/a4e1e7b6f4f8)