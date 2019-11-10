# Cookie笔记
## 什么是Cookie
在网站中，http请求是无状态的，也就是即便第一次登录成功以后，下一次请求服务器，依然不知道你是谁，cookie的出现是为了解决这个问题，第一次登录服务器返回一些数据给浏览器，然后浏览器保存在本地，再次请求的时候就会携带cookie一起发送给服务器。
cookie存储的数据量是有限的，不同的浏览器大小限制不一样，但是一般不超过4kb因此cookie只能存储一些小数据

1. cookie有效期，服务器可以设置cookie有效期，浏览器会自动清除过期的cookie
2. cookie有域名的概念，也就是说浏览器只会把当前域名的相关cookie发送给服务器，而不会携带其他域名的cookie

## flask操作cookie
1. 设置cookie，flask中的cookie是在Response对象上设置的，`flask.Response`有一个`set_cookie`方法，可以通过这个方法设置cookie
2. 删除cookie，Response.delete_cookie(key)方法删除cookie
3. 设置cookie有效期
- max_age，以秒为单位，距现在多少秒后过期
- expires，datetime类型，使用expire需要将值设置为格林尼治时间
- 如果max_age和expires都设置了，以max_age为准
- max_age在IE8以下浏览器是不支持的，expires虽然在新版的HTTP协议中被废弃，但是到目前位置所有的浏览器都支持
- 默认的过期时间是浏览器关闭以后

示例
```python
@app.route('/')
def hello_world():
	resp = Response('python')
	expires = datetime(year=2019,month=10,day=20,hour=14,minute=0,second=0)
	# 格林尼治时间比北京时间晚8小时

	expires = datetime.now()+timedelta(day=30,hour=14)
	resp.set_cookie("language","python")
	return resp
```

4. 设置cookie有效域名，cookie默认只能在主语名下使用，要想cookie能在子域名下使用应该在`set_cookie`时传递一个`domain=.hy.com`
