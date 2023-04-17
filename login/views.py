from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import sqlite3


# Create your views here.
def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, 'register.html')

@csrf_exempt
@require_POST
def userlogin(request):

    conn = sqlite3.connect('db.sqlite3')

    cursor = conn.execute("SELECT id FROM user WHERE account = ? AND password = ?", (request.POST.get('account'),request.POST.get('password')))
    result = cursor.fetchone()

    conn.close()

    if (result):
        request.session['userid'] = result[0]
        return JsonResponse(data = {'result' : True})

    return JsonResponse(data = {'result' : False})

@csrf_exempt
@require_POST
def userregister(request):
    inserted = check_and_insert_user(request.POST.get('account'), request.POST.get('name'), request.POST.get('email'), request.POST.get('password'))
    return JsonResponse(data = {'result' : inserted})

def check_and_insert_user(account, name, email, password):
    conn = sqlite3.connect('db.sqlite3')

    cursor = conn.execute("SELECT name FROM user WHERE name = ?", (name,))
    user_exists = cursor.fetchone() is not None

    inserted = False

    if not user_exists:
        conn.execute("INSERT INTO user (account, name, email, password) VALUES (?, ?, ?, ?)", (account, name, email, password))
        inserted = True

    conn.commit()
    conn.close()

    return inserted

