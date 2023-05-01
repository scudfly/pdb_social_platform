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
    cursor = conn.execute('''
    SELECT u.name, p.content, p.datetime, f.id, u.id = ?, u.id, u.account
    FROM post p 
    JOIN user u ON p.userid = u.id
    LEFT JOIN focus f ON f.userid = ? AND f.focusid = u.id
    ORDER BY p.datetime DESC LIMIT 100;''', (userid, userid,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return render(request, "index.html", {"data_list": rows})

def trend(request):
    userid = request.session.get('userid')
    if not userid:
        return redirect(reverse('login'))

    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.execute('''
    SELECT u.name, p.content, p.datetime, f.id as fid, u.id = ? as uid, u.id, u.account
    FROM post p 
    JOIN user u ON p.userid = u.id
    LEFT JOIN focus f ON f.userid = ? AND f.focusid = u.id
    where fid > 0 OR uid > 0
    ORDER BY p.datetime DESC LIMIT 100;''', (userid, userid,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return render(request, "trend.html", {"data_list": rows})

def focus(request):
    userid = request.session.get('userid')
    if not userid:
        return redirect(reverse('login'))

    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.execute('''
    Select u.id, u.name From [focus] f
    left join [user] u on f.[focusid] = u.[id] 
    where userid = ?;''', (userid,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return render(request, "focus.html", {"data_list": rows})

def post(request):
    userid = request.session.get('userid')
    if not userid:
        return redirect(reverse('login'))

    return render(request, "post.html")

@csrf_exempt
@require_POST
def postContent(request):
    conn = sqlite3.connect('db.sqlite3')
    
    conn.execute("INSERT INTO post (userid, content, datetime) VALUES (?, ?, datetime('now', 'localtime'))", (request.session.get('userid'), request.POST.get('content')))

    conn.commit()
    conn.close()

    return JsonResponse(data = {'result' : True})

@csrf_exempt
@require_POST
def focus_user(request):
    conn = sqlite3.connect('db.sqlite3')
    
    conn.execute("insert into [focus] (userid, focusid) values(?, ?)", (request.session.get('userid'), request.POST.get('focususerid')))

    conn.commit()
    conn.close()

    return JsonResponse(data = {'result' : True})

@csrf_exempt
@require_POST
def unfocus_user(request):
    conn = sqlite3.connect('db.sqlite3')
    
    conn.execute("delete from focus where userid = ? and focusid = ?", (request.session.get('userid'), request.POST.get('focususerid')))

    conn.commit()
    conn.close()

    return JsonResponse(data = {'result' : True})

@csrf_exempt
@require_POST
def logout(request):
    del request.session['userid']
    return JsonResponse(data = {'result' : True})