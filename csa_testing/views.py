from django.shortcuts import render

def home(request):
    context = {}
    return render(request, 'home.html', context)

def buttons_page(request):
    context = {}
    return render(request, 'buttons.html', context)

def sql_page(request):
    context = {}
    return render(request, 'sql_test.html', context)

def fishing_page_doc(request):
    context = {}
    return render(request, 'fishing_doc.html', context)

def fishing_page_test(request):
    context = {}
    return render(request, 'fishing_test/steam_log_in.html')
