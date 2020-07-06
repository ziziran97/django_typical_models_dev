# 第二章 用Django REST framework实现豆瓣API应用

## 2.1豆瓣API功能介绍

豆瓣图书API功能原理是用户通过输入图书的ISBN号（书号）、书名、作者、出版社等部分信息，就可获取到该图书在豆瓣上的所有信息。当然，API中除了包含检索信息之外，还要包含开发者的apikey，有此向开发者收费。

## 2.2 Django REST framework序列化

序列化（Serialization）是指将对象的状态信息转换成可以存储或传输形式的过程。在客户端与服务端传输的数据形式主要分为两种：XML和JSON。在Django中的序列化就是指将对象状态的信息转换为JSON数据，以达到数据信息传送给前端的目的。

序列化是开发API不可缺少的一个环节，Django本身也有一套做序列化的方案，这个方案已经很好了， 但是若跟Django REST framework相比，还是不够极致，速度不够快。

### 2.2.1 Postman的使用

postman可以便捷的想API发送GET、POST、PUT和DELETE请求，几乎是资深或者为自身开发人员调试API的首选。

[下载地址](https://www.getpostman.com/apps)

### 2.2.2 用serializers.Serializer方式序列化

见代码

### 2.2.3 用serializers.ModelSerializer方式序列化

见代码

## 2.3 Django REST framework视图三层封装

见代码

### 2.3.2 用generics.ListAPIView的方式实现视图封装

*注意：* 使用mixins.ListModelMixin+generics.GenericAPIView对APIView进行一次封装，至少需要加一个get函数：

```python
def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)
```

而使用generics.ListAPIView则可以不用加这个函数，因为generics.ListAPIView相对于mixins.ListModelMixin+generics.GenericAPIView而言，所谓的封装，就是封装了一个get函数罢了。

### 2.3.3 用viewsets+Router的方式实现视图封装

*注意：* Django REST framework的权限组件有一个原则，即没有认证就没有权限！所有我们可以看见，在视图类BookModelViewSet中不但加入了permission_classes=[IsDevelop, EnoughMoney],还加入了authentication_classes=[]这样一个空列表。这一行代码是必须加的，如果不加，虽然权限组件依然起作用，但是在权限不通过的时候，detail将不会显示我们定义的message的内容，而永远只是提示未通过。

