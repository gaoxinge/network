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
print root.xpath('//li')
print root.xpath('//li/@class')
print root.xpath('//li/a[@href=\'link1.html\']/text()')
print root.xpath('//li//span/text()')
print root.xpath('//li/a//@class')
print root.xpath('//li[last()]/a/@href')
print root.xpath('//li[last()]/a/@href[1]')
print root.xpath('(//li[last()]/a/@href)[1]')
print root.xpath('//li[last()-1]/a/text()')
print root.xpath('//li[last()-1]/a')[0].text
print root.xpath('//*[@class=\'bold\']')[0].tag
