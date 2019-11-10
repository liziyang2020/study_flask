#CSRF笔记

CSRF（跨站请求伪造）

## CSRF攻击
HTTP请求本身是无状态的，要实现用户的登录，需要使用cookie，这其中就存在漏洞。
当浏览器完成一个网站的登录验证以后，会在本地存储一些验证信息，在这之后访问了一个有CSRF攻击的网站，此网站可以在返回的页面的html中加入一些js，由这些js对之前完成登录验证的网站发起请求，此时浏览器会携带之前网站的验证信息，而服务器无法辨别请求是否是人为操作，这样就产生了CSRF攻击。

## 防御CSRF攻击
CSRF攻击的要点就是在向服务器发送请求的时候，相应的cookie会自动的发送到对应的服务器，造成服务器不知道这个请求是用户发起的还是伪造的，我们可以在用户每次访问有表单的页面的时候，在网页源代码中加一个随机字符串，叫`csrf_token`在cookie中也加入一个相同的值，然后给服务器发送请求的时候，必须在body和cookie中都携带`csrf_token`,只有服务器检测到二者相同，才会通过请求。

主app文件中加入csrf_token防御
```python
from flask import Flask
from flask_wtf import CSRFProtect

app = Flask(__name__)
CSRFProtect(app)
```

表单中加入csrf_token
```
<form action="" method="post">
	<input type="hidden" name="csrf_token" value="{{ csrf_token() }}">
	<tbody>
		<tr>
			<td>email</td>
			<td><input type="text" name="email"></td>
		</tr>

		<tr>
			<td></td>
			<td><input type="submit" id="submit" value="submit"></td>
		</tr>
	</tbody>
</form>
```

- 注意：
	- csrf_token不是直接放在cookie中的，而是先将csrf_token放在session中，进行统一的加密，再放到cookie中，请求页面时，将session返回给服务器，服务器拿到session后，将csrf_token进行解析然后比较。
	- 此处说的cookie和body中的csrf_token一样不是说二者长的一样，而是进行了一系列例如异或等运算的解析以后值的是一样的