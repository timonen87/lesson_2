from django.shortcuts import render
from mainapp.models import Product, ProductCategory


def index(request):

    title = 'geekshop'
    products = Product.objects.all()[:4]


    context = {
        'products': products,
        'title': title,
    }
    return render(request, 'index.html', context=context)


def contacts(request):
    title = 'Контакты'

    location_content = [
        {'city': 'МОСКВА', 'tel': '+7-888-888-8888', 'email': 'info@geekshop.ru', 'adress': 'В пределах МКАД'},
        {'city': 'МОСКВА', 'tel': '+7-888-888-8888', 'email': 'info@geekshop.ru', 'adress': 'В пределах МКАД'},
        {'city': 'МОСКВА', 'tel': '+7-888-888-8888', 'email': 'info@geekshop.ru', 'adress': 'В пределах МКАД'},
    ]

    context = {
        'some_name': 'hello world',
        'title': title,
        'location_content': location_content,
    }
    return render(request, 'contact.html', context=context)