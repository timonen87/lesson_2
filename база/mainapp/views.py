from django.shortcuts import render
from .models import ProductCategory


def products(request, pk=None):
    print(pk)
    title = 'каталог/продукты'


    links_menu = ProductCategory.objects.all()

    related_products = [
        {'href': '/mainapp/img/product-11.jpg', 'name': 'Стул повышенного качества', 'icon_hover':'/mainapp/img/icon-hover.png'},
        {'href': '/mainapp/img/product-21.jpg', 'name': 'Стул повышенного качества', 'icon_hover':'/mainapp/img/icon-hover.png'},
        {'href': '/mainapp/img/product-31.jpg', 'name': 'Стул повышенного качества','icon_hover':'/mainapp/img/icon-hover.png'},
    ]

    context = {
        'links_menu': links_menu,
        'title': title,
        'related_products':related_products,
    }
    return render(request, 'mainapp/products.html', context=context)
