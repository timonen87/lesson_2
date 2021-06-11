from django.shortcuts import render, get_object_or_404
from .models import ProductCategory, Product


def products(request, pk=None):
    print(pk)
    title = 'каталог/продукты'
    links_menu = ProductCategory.objects.all()

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        context = {
            'products': products,
            'title': title,
            'category': category,
            'links_menu': links_menu,

        }
        return render(request, 'mainapp/products.html', context=context)

    products = Product.objects.all()

    context = {
        'products': products,
        'title': title,
        'links_menu': links_menu,
    }

    return render(request, 'mainapp/products.html', context=context)

