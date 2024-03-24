from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from.serializers import productserializer
from . models import product
# Create your views here.
@api_view(['GET'])
def apioverview(request):
    api_urls={
        'List':'/product-list/',
        'Deatil view':'/product-deatil/<int:id>',
        'Create':'/product-create/',
        'Update':'/product-update/<int:id>',
        'Delete':'/product-delete/<int:id>',
    }
    return Response(api_urls)

@api_view(['GET'])
def ShowAll(request):
    products=product.objects.all()
    serializer=productserializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def viewproduct(request,pk):
    singl_product=product.objects.get(id=pk)
    serializer=productserializer(singl_product, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def deleteproduct(request,pk):
    delete_product=product.objects.get(id=pk)
    delete_product.delete()
    return Response('item delete Successfully ')

@api_view(['POST'])
def Createproduct(request):
    serializer=productserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response("Item Create Successfully")

@api_view(['POST'])
def Updateproduct(request,pk):
    products=product.objects.get(id=pk)
    serializer=productserializer(instance=products, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)