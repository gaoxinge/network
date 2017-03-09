from lxml import etree

html = '''
XHTML

<html><body>
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a><a href="link6.html">sixth item</a></li>
</ul>
 </div>

</body></html>
'''

root = etree.HTML(html)
result = root.xpath('//li')
print result[0].xpath('/html')
print result[0].xpath('//a')
print result[0].xpath('a')
print result[4].xpath('a/@href')
print result[0].xpath('@class')
