# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import logout


# Create your views here.
def index(request):
    if 'user_id' in request.session:
        return redirect('/travels')
    return render(request, 'reglogin/index.html')

def register(request):
    result = User.objects.validate_registration(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    # messages.success(request, "Successfully registered!")
    return redirect('/travels')

def login(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    # messages.success(request, "Successfully logged in!")
    return redirect('/travels')

def logout(request):
    del request.session['user_id']
    return redirect('/')

# def dashboard(request):
#     try:
#         request.session['user_id']
#     except:
#         return redirect('/')
#     request.session['user_id']
#     context ={
#         'user': User.objects.get(id=request.session['user_id']),
#         'users': User.objects.all(),
#         'books': Book.objects.all(),
#         'reviews': Review.objects.all()
#     }
#     return render(request, 'bookreview/dashboard.html', context)

# def show(request, user_id):
#     try:
#         request.session['user_id']
#     except:
#         return redirect('/')
#     context = {
#         'user': User.objects.get(id=user_id),
#         # 'reviews': Review.objects.all(),
#         'reviews': Review.objects.filter(reviewer_id=user_id),
#         'books': Book.objects.all()
#     }
#     return render(request, 'bookreview/user.html', context)

# def bookform(request):
#     user = User.objects.get(id=request.session['user_id'])
#     context = {
#         'user': User.objects.get(id=request.session['user_id']),
#         'books': Book.objects.all()
#     }
#     return render(request, 'bookreview/bookform.html', context)

# def add(request):
#     Book.objects.create(
#         title=request.POST['title'],
#         author=request.POST['author']
#     )
#     Review.objects.create(
#         review=request.POST['review'],
#         rating=request.POST['rating'],
#         reviewer=User.objects.get(id=request.session['user_id'])
#     )
#     context = {
#         'user': User.objects.get(id=request.session['user_id'])
#     }
#     return redirect('/dashboard', context)

# def bookpage(request, book_id):
#     context = {        
#         'book': Book.objects.get(id=book_id),
#         'user': User.objects.get(id=request.session['user_id']),
#         'reviews': Review.objects.all()
#     }
#     return render(request,'bookreview/bookpage.html', context)

# def minireview(request, book_id):
#     user = User.objects.get(id=request.session['user_id'])
#     book = Book.objects.get(id=book_id)
#     Review.objects.create(
#         review=request.POST['review'],
#         rating=request.POST['rating'],
#         reviewer=User.objects.get(id=request.session['user_id'])
#     )
#     context = {
#         'user': User.objects.get(id=request.session['user_id']),
#         'book': Book.objects.get(id=book_id)
#     }
#     return redirect('/book/{}/'.format(book_id), context)

# def delete(request, book_id):
#     book = Book.object.get(id=book_id).delete()
#     return redirect('/dashboard')

