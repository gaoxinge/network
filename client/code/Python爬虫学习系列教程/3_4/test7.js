var page = require('webpage').create();
console.log('The default user agent is ' + page.settings.uerAgent);
page.settings.userAgent = 'SpecialAgent';
page.open('http://www.httpuseragent.org', function (status){
	if(status !== 'success'){
		console.log('unable to access network');
	}else{
		var ua = page.evaluate(function (){
			return document.getElementById('myagent').textContent;
		});
		console.log(ua);
	}
	phantom.exit();
});