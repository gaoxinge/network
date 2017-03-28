# 循环

## 对象

```javascript
console.log("number");
for (var x in 123) {
	console.log(x);
}

for (var x in Number(123)) {
	console.log(x);
}

console.log("string");
for (var x in "123") {
	console.log(x);
}

for (var x in String(123)) {
	console.log(x);
}

console.log("object");
for (var x in {1:2,3:4}) {
	console.log(x);
}
```

## 可枚举属性（enumerable属性）

- [js对象中什么是可枚举性(enumerable)？](https://segmentfault.com/a/1190000002953364)
- [关于对象的可枚举属性](https://segmentfault.com/q/1010000003410048?sort=created)

## for...in...和for...of...

```javascript
for (var x of Object.keys(object)) {
    console.log(x + ": " + object[x]);
}
```