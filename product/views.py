from django.utils import timezone

from django.shortcuts import render

from .models import Category, Product, File
from .serializers import CategorySerializers, FileSerializers, ProductSerializes

from subscriptions.models import Subscription

from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class ProductListView(APIView):

    def get(self,request):

        products = Product.objects.all()
        serializer = ProductSerializes(products, many= True, context = {'request':request})
        return Response(serializer.data)
    

class ProductDetailView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, pk):

        if not Subscription.objects.filter(
            user=request.user,
            expire_time__gt=timezone.now()
        ).exists():
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)
        serialiser = ProductSerializes(product, context = {'request': request})
        return Response(serialiser.data)


class CategoryListView(APIView):

    def get(self, request):
        categories = Category.objects.all()
        serialiser = CategorySerializers(categories, many = True, context = {'request': request})
        return Response(serialiser.data)
    
class CategoryDetaileView(APIView):

    def get(self, request, pk):
        try:
            category = Category.objects.get(pk = pk)
        except Category.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)
        serialiser = CategorySerializers(category, context = {'request': request})
        return Response(serialiser.data)
    

class FileListView(APIView):

    def get(self, request, product_id):
        file = File.objects.filter(product_id= product_id)
        serialiser = FileSerializers(file, many = True, context = {'request': request} )
        return Response(serialiser.data)
    

class FileDetaileView(APIView):

    def get(self, request, product_id, pk):
        try:
            files= File.objects.get(pk= pk, product_id= product_id)
        except File.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)
        serialiser = FileSerializers(files, context = {'request': request})
        return Response(serialiser.data)