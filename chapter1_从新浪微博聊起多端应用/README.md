## 1.1 AOP面对切面编程思想

Aspect Oriented Programming -> AOP

在移动互联网时代以来，基于AOP思想，对项目进行前后端分离的基本架构， 已经成为了必要的事情。

## 1.2 Django的前后端分离

Django的普通项目基于MVT模式（Model View Template）
Django的前后端分离项目基于MVVM模式（Model View ViewModel），解耦更彻底，彻底到前后端分离了，甚至可以说分离成了两个项目。

分离原理：后端遵循Restful规范开发API，与前端进行数据交互，实现多端应用。

### 1.2.1 什么是API

可以翻译为数据接口，或者数据接口的使用。

在业内编写这类API，不论是用什么语言，都要遵循RESTful规范。

### 1.2.2 RESTful规范--如何写API

（1）如果是对一个表进行数据操作（增删改查），应该是用一条API，然后根据method的不同，进行不同的操作：

GET、POST、PUT、DELETE、PATCH

（2）面向资源编程，通过API提交的参数最好是名词，比如name，尽量少用动词。

http://www.abc.com/name

（3）体现版本，在API中加入想v1、v2这样的版本代号：

http://www.abc.com/v1/name
http://www.abc.com/v2/name

（4）体现API，让使用者一眼看到这是API而不会是URL，应该在API中加入提示：

http://www.abc.com/api/v1/name
http://www.abc.com/api/v2/name

（5）使用https

https://www.abc.com/api/v1/name
https://www.abc.com/api/v2/name

（6）响应式设置状态码，200和201代表操作成功，403代表权限不够，404代表没有指定资源，500代表运行时发现代码逻辑错误等。

return HttpResponse('adgbag', status=300)

（7）API的参数中加入筛选条件参数，也可以理解为获取资源优先选择GET的方式。

https://www.abc.com/api/v2/name?page=1&size=10

（8）返回值的规范，不同的method操作成功后，后端应该相应的返回值如下：

https://www.abc.com/api/v1/name

不同的提交方式代表对数据的不同的操作：

GET：所有列表

POST：新增的数据

https://www.abc.com/api/v1/name/1

GET:单条数据

PUT：更新，返回更新的数据

PATCH：局部更新，返回更新的数据

DELETE：删除，返回空文档

（9）返回错误信息，应该加入错误代号code，让用户能直接看出是哪种类型的错误。

```Python
ret{
    code:1000,
    data:{{'id':1, 'title':'lala', 'detail':'http://www.'}}
}
```

RESTful规范是业内约定俗成的规范，并不是技术上定义的公式，在实际生产使用中，大家还是要根据业务灵活运用。

### Django REST framework介绍

“使用Python进行web全栈开发者必会Django，使用Django开发前后端分离项目者必会Django REST framework”

Django REST framework的10个常用组件：

- 权限组建
- 认证组件
- 访问频率限制组件
- 序列化组件
- 路由组件
- 视图组件
- 分页组件
- 解析器组件
- 渲染器组件
- 版本组件

[Django REST framework官方文档](https://www.django-rest-framework.org/)

