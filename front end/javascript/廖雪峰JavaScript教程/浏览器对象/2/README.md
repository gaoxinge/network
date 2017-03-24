# DOM

## 更新

```javascript
var js = document.getElementById('p-id'); // <p id="test-js">javascript</p>

js.a = 1; // <p id="test-js">javascript</p>
js.setAttribute('a', '1'); // <p id="test-js" a="1">javascript</p>

js.style.color = '#ff0000'; // <p id="test-js" a="1" style="color: rgb(255, 0, 0);">javascript</p>
```

```javascript
var d = document.createElement('style'); // <style></style>

d.style = 'text/css'; // <style type="text/css"></style>
```

## 插入

### 例子

```html
<head>
	<title>abc</title>
</head>

<body>
<p>a</p>
<div id="list">
	<p id="java">Java</p>
	<p id="python">Python</p>
	<p id="scheme">Scheme</p>
</div>
<p>a</p>
<p>b</p>
<div id="tsil">
</div>
<p>b</p>
</body>
```

```html
<head>
	<title>abc</title>
</head>

<body>
<p>a</p>
<div id="list">
</div>
<p>a</p>
<p>b</p>
<div id="tsil">
	<p id="java">Java</p>
	<p id="python">Python</p>
	<p id="scheme">Scheme</p>
</div>
<p>b</p>
</body>
```

```javascript
// error
var list = document.getElementById('list');
var tsil = document.getElementById('tsil');

for (let i=0, len=list.children.length; i < len; ++i) {
	tsil.appendChild(list.children[i]);
}
```

```javascript
var list = document.getElementById('list');
var tsil = document.getElementById('tsil');

for (let i=0, len=list.children.length; i < len; ++i) {
	tsil.appendChild(list.children[0]);
}
```

### 例子

```html
<head>
	<title>abc</title>
</head>

<body>
<p>a</p>
<div id="list">
	<p id="java">Java</p>
	<p id="python">Python</p>
	<p id="scheme">Scheme</p>
</div>
<p>a</p>
</body>
```

```javascript
// error
var list = document.getElementById('list');

for (let i=0, len=list.children.length; i < len; ++i) {
	list.appendChild(list.children[i]);
}
```

```javascript
var list = document.getElementById('list');

for (let i=0, len=list.children.length; i < len; ++i) {
	list.appendChild(list.children[0]);
}
```