"""book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from users.views import BookAPIView1, BookAPIView2
from users.views import BookMixinView1, BookMixinView2
from users.views import BookModelViewSet

from rest_framework.routers import DefaultRouter
from django.conf.urls import include
router = DefaultRouter()
router.register(r'apibook5', BookModelViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('apibook1/', BookAPIView1.as_view(), name='book1'),
    path('apibook2/', BookAPIView2.as_view(), name='book2'),
    path('apibook3/', BookMixinView1.as_view(), name='book3'),
    path('apibook4/', BookMixinView2.as_view(), name='book4'),
    path('', include(router.urls))
    ]
