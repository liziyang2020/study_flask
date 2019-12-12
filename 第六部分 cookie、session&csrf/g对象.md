# g对象
g是线程隔离的对象，用于保存全局对象。
g对象是在整个Flask应用运行期间都可以使用的，这个对象专门用来存储开发正自己定义的一些数据，方便在整个Flask程序中都可以使用
```python
@app.context_processor
def context_processor():
    if hasattr(g,'user'):
        reutrn {'current_user':g.user}
    else:
        return {}
```