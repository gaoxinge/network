var numbers = [1, 2, 3];
numbers.forEach(function (element, index, array) {
	console.log(index + ": " + element);
});

var str = "Hello World";
Array.prototype.map.call(str, function (element, index, string) {
	console.log(index + ": " + element);
});