var url = 'https://www.baidu.com';
var page = require('webpage').create();
phantom.outputEncoding = 'gbk';
page.open(url, function (status){
	var title = page.evaluate(function (){
		return document.title;
	});
	console.log('page title is ' + title);
	phantom.exit();
});