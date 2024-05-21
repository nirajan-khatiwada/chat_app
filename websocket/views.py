from django.shortcuts import render

# Create your views here.


def index(request,roomname):
    return render(request,"index.html",{'room_id':roomname})