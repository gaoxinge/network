var numbers = [1, 2, 3];
console.log(numbers.map(function (x) {
	return x*x;
}));
console.log(Array.prototype.map.call(numbers, function (x) {
	return x*x;
}));

var str = "Hello World";
console.log(Array.prototype.map.call(str, function (x) {
	return x.charCodeAt(0);
}));


/*
 * parseInt('1', 0, a) = parseInt('1', 0) = 1
 * parseInt('2', 1, a) = parseInt('2', 1) = NaN
 * parseInt('3', 2, a) = parseInt('3', 2) = NaN
 */
var a = ['1', '2', '3'];
console.log(a.map(parseInt));
