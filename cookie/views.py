from django.http import HttpResponse
from django.shortcuts import render
def input(request):
    return render(request,'base.html')
def add(request):
    x=int(request.GET['t1'])
    y=int(request.GET['t1'])
    z=x+y
    resp=HttpResponse('values submit successfully')
    resp.set_cookie('z',z,max_age=100)
    return resp
def display(request):
    if 'z' in request.COOKIES:
        sum = request.COOKIES['z']
        return HttpResponse("addtion of two no:"+sum)
    else:
        return HttpResponse("pls enter values")

