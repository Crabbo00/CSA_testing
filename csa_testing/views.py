from django.db import connection
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import LoginForm

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


def login_sql(request):
    message = ''
    users = []

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['password']

            query = f"SELECT * FROM auth_user WHERE username = '{username}' AND password = '{password}'"

            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()

            if result:
                message = 'Correct Pass'
            else:
                message = 'Incorrect pass'
    else:
        form = LoginForm()

    with connection.cursor() as cursor:
        cursor.execute("SELECT id, username, password, email FROM auth_user LIMIT 10")
        users = cursor.fetchall()

    users = [{'id': u[0], 'username': u[1], 'password': u[2], 'email': u[3]} for u in users]

    context = {'form': form, 'message': message, 'users': users}
    return render(request, 'login_sql.html', context)

def xss_page(request):
    context = {}
    return render(request, 'xss_doc.html', context)

def xss_page_test(request):
    comment = request.GET.get('comment', '').strip()
    comments = request.session.get('comments', [])
    if comment:
        comments.append(comment)
        request.session['comments'] = comments
    return render(request, 'xss_test.html', {
        'comment': comment,
        'comments': comments,
    })

def ddos_page(request):
    context = {}
    return render(request, 'ddos_doc.html', context)


