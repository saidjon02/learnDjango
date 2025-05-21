# store/views.py
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Category
from django.db.models import Count

def queryset_examples(request):
    # 1. Barcha productlarni olish
    all_products = Product.objects.all()

    # 2. Narxi 100 dan katta productlar
    expensive_products = Product.objects.filter(price__gt=100)

    # 3. “Apple” nomli productlar
    apple_products = Product.objects.filter(name="Apple")

    # 4. Narxi 50 dan katta va kategoriya “food” bo‘lgan productlar
    filtered_products = Product.objects.filter(price__gt=50, category__name="food")

    # 5. Narxi 100 dan katta bo‘lganlarni chiqarib tashlash
    cheap_products = Product.objects.exclude(price__gt=100)

    # 6. annotate: Har bir kategoriyada nechta product borligini chiqarish
    categories = Category.objects.annotate(product_count=Count('product'))

    # Natijani ekranga chiqaramiz
    result = "All products with price > 100:<br>"
    for p in expensive_products:
        result += f"- {p.name} | {p.price} so‘m<br>"

    result += "<br>Category count:<br>"
    for c in categories:
        result += f"{c.name} => {c.product_count} ta product<br>"

    return HttpResponse(result)


def home(request):
    # 1. filter(): Narxi 100 dan katta mahsulotlar
    expensive_products = Product.objects.filter(price__gt=100)

    # 2. exclude(): nomi 'Electronics' bo'lmagan kategoriyalar
    non_electronics_categories = Category.objects.exclude(name="Electronics")

    # 3. annotate(): har bir kategoriyadagi mahsulotlar soni
    categories_with_counts = Category.objects.annotate(product_count=Count('product'))

    context = {
        'expensive_products': expensive_products,
        'non_electronics_categories': non_electronics_categories,
        'categories_with_counts': categories_with_counts,
    }

    return render(request, 'home.html', context)
