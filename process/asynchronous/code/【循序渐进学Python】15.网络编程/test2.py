from urllib import urlopen
from urllib import urlretrieve

webpage = urlopen('http://www.cnblogs.com/IProgramming')
txt = webpage.readline(45)
print txt

webpage = urlopen(r'file:D:\H\sr23upd\ADD_ABBR.txt')
txt = webpage.readline(45)
print txt

webpage = urlretrieve('http://www.cnblogs.com/IPrograming/','C:\temp.html')
print webpage