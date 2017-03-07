from lxml import etree

xml = '''
<bookstore>

<book category="COOKING">
  <title lang="en">Everyday Italian</title>
  <author>Giada De Laurentiis</author>
  <year>2005</year>
  <price>30.00</price>
</book>

<book category="CHILDREN">
  <title lang="en">Harry Potter</title>
  <author>J K. Rowling</author>
  <year>2005</year>
  <price>29.99</price>
</book>

<book category="WEB">
  <title lang="chi">XQuery Kick Start</title>
  <author>James McGovern</author>
  <author>Per Bothner</author>
  <author>Kurt Cagle</author>
  <author>James Linn</author>
  <author>Vaidyanathan Nagarajan</author>
  <year>2003</year>
  <price>49.99</price>
</book>

<book category="WEB">
  <title lang="chi">Learning XML</title>
  <author>Erik T. Ray</author>
  <year>2003</year>
  <price>39.95</price>
</book>

</bookstore>
'''

root = etree.XML(xml)
print root.xpath('book')
print root.xpath('/bookstore/book')
print root.xpath('//book')
print root.xpath('/bookstore/book[1]/@category')
print root.xpath('/bookstore/book[last()]/@category')
print root.xpath('/bookstore/book[position()<3]/@category')
print root.xpath('//title[@lang]/@lang')
print root.xpath('//title[@lang=\'chi\']/text()')
print root.xpath('/bookstore/book[price>35.0]//@lang')
