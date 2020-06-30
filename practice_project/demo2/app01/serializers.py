# -*- coding: utf-8 -*-
# @File  : serializers.py
# @Author: ZRSGEEKCABIN
# @Email : ksbc24v@gmail.com
# @Github: https://github.com/ZRSGEEKCABIN
# @Date  : 2020/6/23
# @Desc  : 
from rest_framework import serializers
from .models import Type1, Type2, Type3, Type4, Type

class Type1ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type1
        fields = '__all__'

class Type2ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type2
        fields = '__all__'

class Type3ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type3
        fields = '__all__'

class Type4ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type4
        fields = '__all__'

class TypeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

if __name__ == '__main__':
    pass