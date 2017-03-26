# 语句和表达式

## 上下文无关文法

- Program
  - SourceElements

- SouceElements
  - SouceElement
  - SouceElements SourceElement

- SouceElement
  - Statement
  - FunctionDeclaration

- Statement
  - Block
  - DeclarationsStatement（;）
  - VariableStatement
  - EmptyStatement
  - ExpressionStatement（;）
  - IfStatement
  - IterationStatement
  - ContinueStatement（;）
  - BreakStatement（;）
  - ReturnStatement（;）
  - WithStatement
  - LabelledStatement
  - SwitchStatement
  - ThrowStatement
  - TryStatement
  - DebuggerStatement

## 理解

- 表达式（expression）由运算符（operator）连接
- 语句（statement）由表达式组成，由;结尾

## 区别

### 等于

```javascript
var a;     // declaration statement
var a = 1; // declaration statement
a = 1      // assignment expression
a = 1;     // assignment expression statement
```

### 函数

```javascript
function foo() {console.log(1);}               // function declaration
var foo = function () {console.log(1);};       // function expression（declaration statement）
var foo = new Function('', 'console.log(1)');  // function expression（declaration statement）
```

## 参考

- [JavaScript的表达式语句和表达式](http://www.tuicool.com/articles/7jqAZ3U)
- [Javascript浅谈之表达式和语句的区别](http://biancheng.dnbcw.net/javascript/465725.html)
- [JavaScript中:表达式和语句的区别](http://www.cnblogs.com/ziyunfei/archive/2012/09/16/2687589.html)