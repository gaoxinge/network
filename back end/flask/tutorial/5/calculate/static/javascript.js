var pos = 4;
function calculate() {
	var code;
	if(window.event)     code = event.keyCode;
	else if(event.which) code = event.which;
	if (code !== 13)     return;
		
	var request = new XMLHttpRequest();
	request.onreadystatechange = function () {
	if (request.readyState === 4) {
		var textarea = document.getElementsByTagName('textarea')[0];
		textarea.removeAttribute('readonly');
		var tmp = '\n>>> ' + JSON.parse(request.responseText)['result'] + '\n>>> ';
		textarea.value += tmp;
		pos += tmp.length;
		}
	};
		
	var textarea = document.getElementsByTagName('textarea')[0];
	textarea.setAttribute('readonly', 'readonly');
	var data = textarea.value.slice(pos);
	pos += data.length;
	var formData = new FormData();
	formData.append('expression', data);
	request.open('POST', '/calculate');
	request.send(formData);
}