# 内建类型

## 基本类型

- 基本类型包含于内建类型

### 分类一

- 这是周爱民的分类方法，基于typeof，类似于元类-类-实例

```javascript
console.log(typeof(undefined));      // undefinded
console.log(typeof(1));              // number
console.log(typeof("1"));            // string
console.log(typeof(true));           // boolean
console.log(typeof(Symbol('know'))); // symbol
console.log(typeof({1:"1"}));        // object
console.log(typeof(Symbol));         // function
```

### 分类二

- 这是ecma的分类方法，基于isinstance，类似于函数对象-普通对象
- undefined
- null
- number
- string
- boolean
- symbol
- object

## 内建类型

## 分类一

- 元类
  - Function
- 类
  - Number
  - Boolean
  - String
  - Array
  - Map
  - Set
  - Date
  - RegExp
  - Error
  - Object
- 实例
  - Math
  - JSON

## 分类二

- 函数对象
  - Function
  - Number
  - Boolean
  - String
  - Array
  - Map
  - Set
  - Date
  - RegExp
  - Error
  - Object
- 普通对象
  - Math
  - JSON