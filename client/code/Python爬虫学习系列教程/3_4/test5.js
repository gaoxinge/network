var page = require('webpage').create();

/*
page.open('https://www.baidu.com', function (){
	page.render('github.png');
	phantom.exit();
});*/

page.viewportSize = {width: 1024, height: 768};
page.clipRect = {top: 0, left: 0, width:1024, height: 768};
page.open('https://www.baidu.com', function (){
	page.render('germy.png');
	phantom.exit();
});