from django.shortcuts import render
# 引入序列化类
from .serializers import Type1ModelSerializer, Type2ModelSerializer
from .serializers import Type3ModelSerializer, Type4ModelSerializer
from .serializers import TypeModelSerializer
# 引入数据表
from .models import Type1, Type2, Type3, Type4, Type

# 引入rest_framework相关模块
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
# Create your views here.
class Type1View(APIView):
    '''
    all Type1
    '''
    renderer_classes =  [JSONRenderer]
    def get(self, request, format=None):
        Types = Type1.objects.all()
        Types_serializer = Type1ModelSerializer(Types, many=True)
        return Response(Types_serializer.data)

class Type2View(APIView):
    '''
    all Type2
    '''
    renderer_classes = [JSONRenderer]
    def get(self, request, format=None):
        Types = Type2.objects.all()
        Types_serializer = Type2ModelSerializer(Types, many=True)
        return Response(Types_serializer.data)


class Type3View(APIView):
    '''
    all Type3
    '''
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        Types = Type3.objects.all()
        Types_serializer = Type3ModelSerializer(Types, many=True)
        return Response(Types_serializer.data)


class Type4View(APIView):
    '''
    all Type4
    '''
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        Types = Type4.objects.all()
        Types_serializer = Type4ModelSerializer(Types, many=True)
        return Response(Types_serializer.data)

class TypeView(APIView):
    '''
    操作类别表
    '''
    renderer_classes = [JSONRenderer]
    def get(self, request, format=None):
        types = Type.objects.all()
        types_serializer = TypeModelSerializer(types, many=True)
        return Response(types_serializer.data)
    def post(self, request):
        name = request.data.get('name')
        category_type = request.data.get('lei')
        parent_category_id = request.data.get('parent')
        type = Type()
        type.name = name
        type.category_type = category_type
        if parent_category_id:
            parent_category = Type.objects.filter(id=parent_category_id).first()
            type.parent_category = parent_category
        type.save()
        type_serializer = TypeModelSerializer(type)
        return Response(type_serializer.data)