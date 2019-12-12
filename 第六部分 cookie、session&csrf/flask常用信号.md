# Flask信号
## 自定义Flask信号

自定义信号的步骤分为3步，
- 定义信号 定义信号需要用到blinker包中的Namespace

示例
```python
# Namespace的作用，为了防止多人开发时，信号命名的冲突
from blinker import Namespace
mysignal = Namespace()
visit_signal = mysignal.signal('visit_signal')
```

- 监听信号 监听信号使用signal对象的connect方法，这个方法需要传递一个函数用来接收以后监听到这个信号时应该做的操作

示例
```python
def visit_func(sender,username):
    print(sender)
    print(username)

mysignal.connect(visit_func)
```
- 发送信号 发送信号使用的是signal对象的send方法，这个方法可以传递一些其他参数过去

示例
```python
mysignal.send(username='user1')
```
## Flask内置信号

1. template_rendered：模板渲染完毕后发送

```python
from flask import template_rendered
def log_template_renders(sender,template,context,*args)
    print('sender:',sender)

template_rendered.connect(log_template_renders,app)
```
2. before_render_template 模板渲染之前的信号
3. request_started 模板开始渲染
4. request_finished 模板渲染完成
5. request_tearing_down request对象被销毁的信号
6. got_request_expection 视图函数发生异常的信号，一般可以监听这个信号记录网站异常信息
7. appcontext_tearing_down app上下文被销毁的信号
8. appcontext_pushed app上下文被压入栈中的信号
9. appcontext_poped app上下文被从栈中弹出的信号
10. message_flashed 调用了Flask的`flashed`方法的信号
        