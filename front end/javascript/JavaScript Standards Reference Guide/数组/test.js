var obj = {
	0: 10,
	1: 20,
	2: 30,
	length: 3
};

arr = Array.from(obj);
console.log(arr instanceof Array);

var arr = Array.prototype.slice.call(obj);
console.log(arr instanceof Array);

console.log(Array.prototype.map.call(obj, function (x) {
	return x*x;
}));

Array.prototype.forEach.call(obj, function (element, index, string) {
	console.log(index + ": " + element);
});