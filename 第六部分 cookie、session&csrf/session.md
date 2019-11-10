# session笔记
## 理论
1. session的基本概念
session和cookie有点类似，都是为了存储相关的用户信息，不同的是，cookie是存储在本地浏览器，而session是存储在服务器端，需要注意的是，cookie是一项技术，而session只是一个概念，一个服务器存储授权信息的解决方案，不同的框架和语言有不同的实现方式，但都是为了解决cookie存储数据不安全的问题。
2. session与cookie的结合使用
- session存储在服务器端，可以使用mysql、redis memcached等存储
- 原理：客户端发送验证信息，服务器验证成功后，把验证信息存放在session中，然后随机生成一个唯一的session_id，再将session_id存放在cookie中返回给浏览器，以后浏览器携带并通过session_id在服务器中找到相关的验证信息。
- session可以存储到客户端，原理是客户端发送验证信息，服务器把验证信息使用严格的加密方式进行加密，再把加密后的信息存储到cookie，返回给浏览器，以后浏览器发送请求，服务器拿到cookie后，就从cookie找到那个加密的信息

## flask操作session
1. 设置session，通过`flask.session`可以操作session，操作session和操作字典是一样的
	`session['key']=value`
2. 获取session，同样类似字典
	`session.get(key)`
3. 删除session中的值，同样类似字典
	`session.pop(key)`
	`del session[key]`
	`session.clear()`清除所有session
4. 设置session有效期
	默认有效期是浏览器关闭以后
	如果设置了`session.permanent=True`则默认31天后过期，如果不想在31天后过期，可以设置`app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hour=2)`两小时后过期
