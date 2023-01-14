from django.shortcuts import render

from .models import Category, Product, Order

from .forms import OrderForm

from rest_framework import viewsets

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


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer



