# proxy

## 原理

浏览器把要访问的服务器域名告诉本地代理，直接发送请求给国外的代理服务器。代理服务器在与目标服务器连接时，做dns解析，发送请求，返回数据。下面罗列一些代理类型：

- ssl
- http/https：goagent，[goproxy](https://github.com/phuslu/goproxy)，[XX-Net](https://github.com/XX-net/XX-Net)
- socks5：[shadowsocks](https://github.com/shadowsocks)，[Long-live-shadowsocks](https://github.com/Long-live-shadowsocks)

## 方法

具体可参见

- [goproxy](https://github.com/phuslu/goproxy)
- [XX-Net](https://github.com/XX-net/XX-Net)
- [shadowsocks](https://github.com/shadowsocks)
- [Long-live-shadowsocks](https://github.com/Long-live-shadowsocks)