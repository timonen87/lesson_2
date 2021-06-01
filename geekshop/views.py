from django.shortcuts import render


def index(request):
    title = 'Интернет магазин'


    tab_content = [
        {'href': '/img/product-1.jpg', 'name': 'Отличный стул', 'icon_hover': '/img/icon-hover.png'},
        {'href': '/img/product-3.jpg', 'name': 'Отличный чайник','icon_hover': '/img/icon-hover.png'},
        {'href': '/img/product-3-sm.jpg', 'name': 'Отличный диван', 'icon_hover': '/img/icon-hover.png'},
        {'href': '/img/product-2.jpg', 'name': 'Стул повышенного качества', 'icon_hover': '/img/icon-hover.png'},
    ]

    context = {
        'tab_content': tab_content,
        'title': title,
    }
    return render(request, 'index.html', context=context)

def contacts(request):
    title = 'Контакты'

    context = {
        'some_name': 'hello world',
        'title': title,
    }
    return render(request, 'contact.html', context=context)