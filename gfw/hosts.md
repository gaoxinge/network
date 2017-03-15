# hosts

## 原理

主机访问网站首先要将域名解析成IP，过程如下：主机发送域名，hosts将其解析成IP，DNS进一步解析（如果hosts没有解析），最后发送至目标服务器。而GFW有两种封锁方式：第一种，DNS污染：某些域名在DNS解析时，返回错误的IP；另一种，IP封锁：阻止你访问一些特定的IP地址。hosts翻墙就是找到可用的IP（没有被封锁的IP地址），然后将其添加到hosts文件（绕过DNS污染）。

## 方法

你可以通过[google hosts](https://coding.net/u/scaffrey/p/hosts/git/raw/master/hosts)找到最新的google hosts。