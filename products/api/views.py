from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.db.models import Q
from django.db import connection

from products.models import (
    Categories,
    Option,
    Product
)

from .serializers import (
    CategoriesSerializer,
    OptionSerializer,
    ProductSerializer
)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def list_of_cattegories(request, pk=None):
    if request.method == 'GET':
        if pk is None:
            categories = Categories.objects.all()
            serialized_data = CategoriesSerializer(categories, many=True)
        else:
            category = Categories.objects.get(pk=pk)
            serialized_data = CategoriesSerializer(category)
        return Response(data={"data" : serialized_data.data}, status=status.HTTP_201_CREATED)

    if request.method == 'POST':
        parsed_data = JSONParser().parse(request)
        input = CategoriesSerializer(data=parsed_data)
        if input.is_valid():
            input.save()
            return Response(data="item saved", status=status.HTTP_201_CREATED)

    if request.method == 'PUT':
        parsed_data = JSONParser().parse(request)
        if pk is not None:
            category = Categories.objects.get(pk=pk)
            serializer = CategoriesSerializer(category, data=parsed_data)
            if serializer.is_valid():
                serializer.save()
                return Response(data={"status": "Updated"}, status=status.HTTP_202_ACCEPTED)
            return Response(data={'status': 'something went wrong.'}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        try:
            category = Categories.objects.get(pk=pk)
            if category is not None:
                category.delete()
                return Response(data={'status': 'Deleted.'}, status=status.HTTP_202_ACCEPTED)
        except category.DoseNotExist:
            raise Exception('Object is not existed. Please try with another id')


    return Response(data={'status': 'Invalid request.'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def products(request):
    if request.method == 'GET':
        products = Product.objects.select_related('category').get(id=1)
        for product in products:
            print(product.category.name)
        if products:
            serialized_data = ProductSerializer(products, many=True)
            return Response(data=serialized_data.data, status=status.HTTP_200_OK)
        else:
            return Response(data="No data", status=status.HTTP_200_OK)


class Options(APIView):

    def get(self, request, format=None):
        options = Options.objects.all()
        serialized_data = OptionSerializer(data=options, many=True)
        return Response(data=serialized_data.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serialized_data = OptionSerializer(request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(data="Option created")
        return Response(data="validation error")






