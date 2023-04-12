from django.shortcuts import render
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

    cursor = conn.execute("SELECT name FROM user WHERE name = ? AND password = ?", (request.POST.get('username'),request.POST.get('password')))
    user_exists = cursor.fetchone() is not None

    conn.close()

    return JsonResponse(data = {'result' : user_exists})

@csrf_exempt
@require_POST
def userregister(request):
    inserted = check_and_insert_user(request.POST.get('username'), request.POST.get('email'), request.POST.get('password'))
    return JsonResponse(data = {'result' : inserted})

def check_and_insert_user(name, email, password):
    conn = sqlite3.connect('db.sqlite3')

    cursor = conn.execute("SELECT name FROM user WHERE name = ?", (name,))
    user_exists = cursor.fetchone() is not None

    inserted = 'false'

    if not user_exists:
        conn.execute("INSERT INTO user (name, email, password) VALUES (?, ?, ?)", (name, email, password))
        inserted = 'true'

    conn.commit()
    conn.close()

    return inserted

