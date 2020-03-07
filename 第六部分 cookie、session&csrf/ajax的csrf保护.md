#Ajax笔记
## ajax的使用步骤
1. 创建一个异步对象
2. 设置请求方式和请求地址
3. 发送请求
4. 监听状态变化
5. 处理返回结果

## 原生ajax
```html
<!DOCTYPE html>
<html lang    ="en">
<head>
<meta charset ="UTF-8">
<title>Document</title>
</head>
<body>

<script>
	window.onload = function(ev){
	var oBtn      = document.querySelector("button");
	oBtn.onclick  = function(ev1){
		// 创建一个异步对象
		var xmlhttp   = XMLHttpRequest();
		// 设置请求方式和请求地址
			// method：请求的类型；GET 或 POST
			// url：文件在服务器上的位置
			// async：true（异步）或 false（同步）
		xmlhttp.open("GET","url",true);
		// 发送请求
		xmlhttp.send();
		// 监听状态变化
			// 0: 请求未初始化
			// 1: 服务器连接已建立
			// 2: 请求已接收
			// 3: 请求处理中
			// 4: 请求已完成，且响应已就绪
		xmlhttp.onreadystatechange = function(ev2){
			if(xmlhttp.readyState==4){
				// 判断请求是否成功
				if(xmlhttp.status >= 200 && xmlhttp.status < 300 || xmlhttp.status == 304){
					// 处理返回结果
				}else{
					//没有接收到服务器数据
				}
			}
		}

	}
}
</script>
</body>
</html>

```
[详细内容请看](https://www.bilibili.com/video/av22807707/?p=146&t=593 "李南江教授ajax")

## 使用jq.ajax

使用jQuery提供的ajax方法需要在使用前引入jquery
```js
$($function(){
	$("#submit").click(function(event){
		event.prevenDefault();
		var email = $("input[name=email]").val();
		var csrf_token = $("input[name=csrf_token]").val();

		$.post({
			"url":"/login/"
			"data":{
				"email":email,
				"csrf_token":csrf_token
			},
			"success": function(){
				// some code...
			},
			"fail": function(){
				// some code...
			}

		});
	});
});
```

另一种更方便的写法，推荐在meta标签中渲染csrf
```html
<meta name="csrf_token" content="{{ csrf_token() }}">
```
如果要发送ajax请求，则在发送之前添加csrf
```js
var csrftoken = $("meta[name=csrf_token]").attr("content");
$.ajaxSetup({
	"beforeSend": function(xhr,settings){
		if(!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
			xhr.setRequestHeader("X-CSRFToken",csrftoken);
		}
	}
});
```

封装ajax
<!-- myajax.js -->
```js
var myAjax = {
	"get": function(args) {
		args["method"] = "get";
		this.ajax(args);
	},
	"post": function(args) {
		args["method"] = "post";
		this.ajax(args);
	},
	"ajax": function(args) {
		this._ajaxSetup();
		$.ajax(args);
	},
	"_ajaxSetup": function() {
		$.ajaxSetup({
			"beforeSend": function(xhr,settings){
				if(!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
					var csrftoken = $("meta[name=csrf_token]").attr("content");
					xhr.setRequestHeader("X-CSRFToken",csrftoken);
				}
			}
		});
	}
};
```

使用自定义的ajax
```js
$.myAjax({
	"url":"/login/"
	"data":{
		"email":email,
	},
	"success": function(){
		// some code...
	},
	"fail": function(){
		// some code...
	}
```
