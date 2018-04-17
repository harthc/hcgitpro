from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from app01.models import *
from datetime import date
from django.db.models import Q, F
from django.views.generic import View

# Create your views here.


def showbook(request):
    books = BookInfo.objects.all()
    print(request.path)
    return render(request, 'app01/showbook.html', {'books': books})


def add(request):
    book = BookInfo()
    book.title = '越女剑'
    book.pub_time = date(1990, 1, 1)
    book.save()
    return HttpResponseRedirect('/showbook')


def delete(request, book_id):
    BookInfo.objects.get(id=book_id).delete()
    # delete(book)
    return redirect('/showbook')


def select(requset):
    books = BookInfo.objects.filter(read__gt=F('comment')*8)
    return render(requset, 'app01/select.html', {'books': books})


class Sb(View):
    def get(self, request):
        return HttpResponse('hello')

    def post(self, request):
        return HttpResponse('python')