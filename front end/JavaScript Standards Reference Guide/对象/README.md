# 对象

## 属性

- 值
- 可写
- 可枚举
- 可配置
- 如何设置
- 如何读取

## 默认

- 可写：true
- 可枚举：true
- 可配置：true
- 如何设置：undefinded
- 如何读取：undefinded

## 定义

- 方式：默认设置，Object.defineProperty和Object.defineProperties，不可二次定义
- Object.definPropery和Object.defineProperties：值，可写，可枚举，可配置与如何设置，如何读取不能同时定义

## 查看

- obj.xxx：xxx为标识符
- obj[xxx]：xxx为数字，加引号的数字或标识符
- Object.getOwnPropertyDescriptor(obj, xxx)：可以查看属性xxx的描述
- obj.propertyisEnumerable(xxx)：可以查看属性xxx是否可枚举
- Object.keys(obj)：可以查看所有可枚举的固有属性
- Object.getOwnPropertyNames(obj)：可以查看所有的固有属性
- obj.hasOwnProperty(xxx)：可以查看xxx是否是obj的固有属性
- xxx in obj：可以查看xxx是否在obj的原型链中


## 参考

- [js对象中什么是可枚举性(enumerable)？](https://segmentfault.com/a/1190000002953364)
- [javascript中的面向对象理解（一）](http://blog.csdn.net/u014516981/article/details/52865035)
- [javaScript工作必知(八) 属性的特性 值、写、枚举、可配置](http://www.cnblogs.com/fandong90/p/5543653.html)
- [javascript中对象的属性的特性](http://www.cnblogs.com/yugege/p/4823863.html)