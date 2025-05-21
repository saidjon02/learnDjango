# myapp/views.py
from django.shortcuts import render
from .models import Product, Category
from django.db.models import Count, Avg

def home(request):
    # filter: faqat narxi 50 dan katta bo'lganlar
    filtered_products = Product.objects.filter(price__gt=50)

    # exclude: nomida "apple" bo'lmaganlar
    excluded_products = Product.objects.exclude(name__icontains='apple')

    # annotate: har bir Category uchun nechta product borligini chiqarish
    categories_with_count = Category.objects.annotate(product_count=Count('product'))

    # aggregate: o‘rtacha narxni chiqarish
    average_price = Product.objects.aggregate(Avg('price'))

    return render(request, 'home.html', {
        'filtered_products': filtered_products,
        'excluded_products': excluded_products,
        'categories_with_count': categories_with_count,
        'average_price': average_price,
    })
