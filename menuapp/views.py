from django.shortcuts import render

def index(request):
    return render(request, 'menuapp/home.html')

def about(request):
    return render(request, 'menuapp/about.html')


def index2(request):
    return render(request, 'menuapp/index.html')



def base(request):
    return render(request, 'menuapp/base.html')


def funk(request):
    return render(request, 'menuapp/menu_node.html')



def funk2(request):
    return render(request, 'menuapp/menu_draw.html')