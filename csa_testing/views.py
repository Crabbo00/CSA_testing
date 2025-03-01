from django.shortcuts import render

def home(request):
    context = {}
    return render(request, 'home.html', context)

def buttons_page(request):
    context = {}
    return render(request, 'buttons.html', context)

def sql_page(request):
    context = {}
    return render(request, 'sql.html', context)
