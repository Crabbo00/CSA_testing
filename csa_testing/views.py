from django.db import connection
from django.http import JsonResponse
from django.shortcuts import render, redirect
def home(request):
    context = {}
    return render(request, 'home.html', context)

def buttons_page(request):
    context = {}
    return render(request, 'buttons.html', context)

def sql(request):
    if request.method == 'POST' and 'query' in request.POST:
        query = request.POST['query']
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                if query.strip().lower().startswith('select'):
                    results = cursor.fetchall()
                    return JsonResponse({'results': results})
                return JsonResponse({'message': 'Query executed successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return render(request, 'sql.html')

def fishing_page_doc(request):
    context = {}
    return render(request, 'fishing_doc.html', context)


def fishing_page_test(request):
    if request.method == 'POST':
        request.session['username'] = request.POST.get('username')
        request.session['password'] = request.POST.get('password')
        return redirect('fishing_result')

    return render(request, 'fishing_test/steam_log_in.html')

def fishing_result(request):
    username = request.session.get('username')
    password = request.session.get('password')

    context = {
        'username': username,
        'password': password
    }
    return render(request, 'fishing_test/result.html', context)


