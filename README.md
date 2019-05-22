# web-traceroute
Web traceroute looking glass (Bash CGI)(自己写自己用的)

支持traceroute和besttrace

# 文件
前端服务器：server文件夹

节点服务器：node文件夹

# 环境要求
Bash + 支持CGI的Web服务器 + Curl + traceroute/besttrace


# 常见问题
权限不足：给traceroute或者besttrace加上SUID权限

无输出：检查参数是否正确，或者在无IPv6的服务器上请求了IPv6地址

# 关于

a@ghzgqx.com 2019.5.22

版权没有 盗版不究 有bug自己改别找我就那么几行代码
