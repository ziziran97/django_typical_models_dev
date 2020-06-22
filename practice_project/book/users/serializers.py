# -*- coding: utf-8 -*-
# @File  : serializers.py
# @Author: ZRSGEEKCABIN
# @Email : ksbc24v@gmail.com
# @Github: https://github.com/ZRSGEEKCABIN
# @Date  : 2020/6/19
# @Desc  : 
from rest_framework import serializers
from .models import UserProfile, Book

class BookSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, max_length=100)
    isbn = serializers.CharField(required=True, max_length=100)
    author = serializers.CharField(required=True, max_length=100)
    publish = serializers.CharField(required=True, max_length=100)
    rate = serializers.FloatField(default=0)

class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        #fields = '__all__'  # 将整个表的所有字段都序列化
        fields = ('title', 'isbn', 'author')    # 指定序列化某字段

if __name__ == '__main__':
    pass