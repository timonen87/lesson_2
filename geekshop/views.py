from django.shortcuts import render


def index(request):
    title = 'Интернет магазин'


    tab_content = [
        {'href': '/img/product-1.jpg', 'name': 'Отличный стул'},
        {'href': '/img/product-3.jpg', 'name': 'Отличный чайник'},
        {'href': '/img/product-3-sm.jpg', 'name': 'Отличный диван'},
        {'href': '/img/product-2.jpg', 'name': 'Стул повышенного качества'},
    ]

    context = {
        'tab_content': tab_content,
        'some_name': 'hello world',
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