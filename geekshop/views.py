from django.shortcuts import render


def index(request):
    title = 'Интернет магазин'
    list_params = ['стул', 'стол', 'купить']

    context = {
        'list_params': list_params,
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