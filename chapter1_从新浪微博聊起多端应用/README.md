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