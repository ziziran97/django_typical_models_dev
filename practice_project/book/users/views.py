from django.shortcuts import render
from .serializers import BookSerializer
from .serializers import BookModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserProfile, Book
from rest_framework import mixins
from rest_framework import generics

# Create your views here.


class BookAPIView1(APIView):
    '''
    使用Serializer
    '''
    def get(self, request, format=None):
        APIKey = self.request.query_params.get('apikey', 0)
        developer = UserProfile.objects.filter(APIkey=APIKey).first()
        if developer:
            balance = developer.money
            if balance > 0:
                isbn = self.request.query_params.get('isbn', 0)
                books = Book.objects.filter(isbn=int(isbn))
                books_serializer = BookSerializer(books, many=True)
                developer.money -= 1
                developer.save()
                return Response(books_serializer.data)
            else:
                return Response('钱不够，快给钱！')
        else:
            return Response('你没注册')
        
class BookAPIView2(APIView):
    '''
    使用ModelSerializer
    '''
    def get(self, request, format=None):
        APIKey = self.request.query_params.get('apikey', 0)
        developer = UserProfile.objects.filter(APIkey=APIKey).first()
        if developer:
            balance = developer.money
            if balance > 0:
                isbn = self.request.query_params.get('isbn', 0)
                books = Book.objects.filter(isbn=int(isbn))
                books_serializer = BookModelSerializer(books, many=True)
                developer.money -= 1
                developer.save()
                return Response(books_serializer.data)
            else:
                return Response('兄弟，充钱！')
        else:
            return Response('快去注册')

class BookMixinView1(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    def get(self, request, *args, **kwargs):    # 这里不加get函数，代表默认不支持get访问这个api，所以必须加上
        APIKey = self.request.query_params.get('apikey', 0)
        developer = UserProfile.objects.filter(APIkey=APIKey).first()
        if developer:
            balance = developer.money
            if balance > 0:
                isbn = self.request.query_params.get('isbn', 0)
                developer.money -= 1
                developer.save()
                self.queryset = Book.objects.filter(isbn=int(isbn))
                return self.list(request, *args, **kwargs)
            else:
                return Response('冇钱啊，兄dei')
        else:
            return Response('先注册吧')

class BookMixinView2(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    def get(self, request, *args, **kwargs):
        APIKey = self.request.query_params.get('apikey', 0)
        developer = UserProfile.objects.filter(APIkey=APIKey).first()
        if developer:
            balance = developer.money
            if balance > 0:
                isbn = self.request.query_params.get('isbn', 0)
                developer.money -= 1
                developer.save()
                self.queryset = Book.objects.filter(isbn=int(isbn))
                return self.list(request, *args, **kwargs)
            else:
                return Response('冇钱啊，大兄弟')
        else:
            return Response('注册先')