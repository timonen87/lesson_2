from django.shortcuts import render


def products(request):
    title = 'каталог/продукты'

    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'mainapp:index', 'name': 'офис'},
        {'href': 'mainapp:index', 'name': 'модерн'},
        {'href': 'mainapp:index', 'name': 'классика'},
    ]

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
