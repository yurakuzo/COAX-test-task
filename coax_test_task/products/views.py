from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Product, Order

from .forms import OrderForm

from rest_framework import viewsets, permissions, status

from .serializers import OrderSerializer


def listing(request):
    categories = Category.objects.all()
    if request.GET.get('category'):
        category = request.GET.get('category')
        listings = Product.objects.filter(category__name=category)
    else:
        listings = Product.objects.all()
    context = {
        "categories": categories,
        "listings": listings,
    }
    return render(request, 'products/listing.html', context=context)


def create_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(**form.cleaned_data)
            order.save()
    else:
        form = OrderForm()
    context = {
        "form": form,
    }
    return render(request, "products/create_order.html", context=context)


@api_view(('POST',))
def create_order_jQuery(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        context = {'form': form}
        data = {
            'username': request.POST['username'],
            'email': request.POST['email'],
            'product': request.POST['product'],
        }
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        form = OrderForm()
        context = {
            "form": form,
        }
    return render(request, "products/create_order_jQuery.html", context=context)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# class OrderAPIViewSet(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get(self, request, *args, **kwargs):
#         orders = Order.objects.all()
#         serializer = OrderSerializer(orders, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request, *args, **kwargs):
#         data = {
#             'username': request.user.username,
#             'email': request.data.get('email'),
#             'product': request.data.get('product')
#         }
#         serializer = OrderSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
