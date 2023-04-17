from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import sqlite3

def index(request):
    userid = request.session.get('userid')
    if not userid:
        return redirect(reverse('login'))

    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.execute("SELECT u.name, p.content, p.datetime FROM post p JOIN user u ON p.userid = u.id ORDER BY p.datetime DESC LIMIT 10;")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return render(request, "index.html", {"data_list": rows})

def post(request):
    userid = request.session.get('userid')
    if not userid:
        return redirect(reverse('login'))

    return render(request, "post.html")

@csrf_exempt
@require_POST
def postContent(request):
    conn = sqlite3.connect('db.sqlite3')
    
    conn.execute("INSERT INTO post (userid, content, datetime) VALUES (?, ?, datetime('now'))", (request.session.get('userid'), request.POST.get('content')))

    conn.commit()
    conn.close()

    return JsonResponse(data = {'result' : True})
