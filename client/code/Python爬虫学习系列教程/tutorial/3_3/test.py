from lxml import etree

xml = '''
<bookstore>
	<book>
		<title lang="eng">Harry Potter</title>
		<price>29.99</price>
	</book>

	<book>
		<title lang="chi">Learning XML</title>
		<price>39.95</price>
	</book>
</bookstore>
'''

html = '''
<html>
	<body>
		<div>
			<ul>
				<li class="item-0"><a href="link1.html">first item</a></li>
				<li class="item-1"><a href="link2.html">second item</a></li>
				<li class="item-inactive"><a href="link3.html">third item</a></li>
				<li class="item-1"><a href="link4.html">fourth item</a></li>
				<li class="item-0"><a href="link5.html">fifth item</a></li>
			</ul>
		</div>
	</body>
</html>
'''
    
root = etree.XML(xml)
print etree.tostring(root)
print '-------------------------'
root = etree.parse('hello.xml')
print etree.tostring(root)
print '-------------------------'
root = etree.HTML(html)
print etree.tostring(root)
print '-------------------------'
root = etree.parse('hello.html')
print etree.tostring(root)
