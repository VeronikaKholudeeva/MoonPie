import stripe
from select import select
from django.db.models import Q

from django.http import Http404
from rest_framework import serializers

from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render

from rest_framework import status, authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes,renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from sympy import product, uppergamma

from .models import Base, Taste
from .models import Product
from .serializers import ProductSerializer

from .models import Review
from .serializers import ReviewSerializer

from .models import Order
from .serializers import OrderSerializer, MyOrderSerializer


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])





















def checkout(request):
    
    serializer = OrderSerializer(data=request.data)
   
    if serializer.is_valid():
        stripe.api_key = settings.STRIPE_SECRET_KEY
        paid_amount = sum(item.get('quantity')*item.get('product').price for item in serializer.validated_data['items'])
        
        try:
            charge = stripe.Charge.create(
                amount=int(paid_amount),
                currency= 'USD',
                description='Заказ в MoonPie',
                source=serializer.validated_data['stripe_token']
            )
            
            serializer.save(user=request.user, paid_amount=paid_amount)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = MyOrderSerializer(orders, many=True)
        return Response(serializer.data)





























class getProduct(APIView):
    def get(self, request, format=None):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)


class gethotProduct(APIView):
    def get(self, request, format=None):
        product = Product.objects.filter(
            Q(id=15) | Q(id=11) | Q(id=21) | Q(id=13))
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)


class getReview(APIView):
    def get(self, request, format=None):
        review = Review.objects.all()
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data)


class getLastReview(APIView):
    def get(self, request, format=None):
        review = Review.objects.all().order_by('-id')[1:5]
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    def get_object(self, taste_slug, base_slug, product_slug):
        try:
            return Product.objects.filter(taste__slug=taste_slug, base__slug=base_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, taste_slug, base_slug, product_slug, format=None):
        product = self.get_object(taste_slug, base_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


@api_view(('POST', 'GET'))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def search(request):
    query = request.data.get('query', '')
    search = query.upper()
    products = []
    if query:
        for prod in Product.objects.all():
            text = str(prod.description + prod.name).upper()
            if search in text:
                products += Product.objects.filter(name=prod)
                serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})


@api_view(('POST', 'GET'))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def filterbybase(request):
    query = request.data.get('checks', '')
    query2 = request.data.get('checks2', '')
    products = Product.objects.all()
    if query or query2:
        p1 = []
        p2 = []
        for i in range(0, len(query)):
            p1 += Product.objects.filter(base=query[i])
        for j in range(0, len(query2)):
            p2 += Product.objects.filter(taste=query2[j])
        if p1 and p2:
            products = list(set(p1) & set(p2))
        else:
            if p1:
                products = p1
            else:
                products = p2
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response(ProductSerializer(products, many=True).data)
