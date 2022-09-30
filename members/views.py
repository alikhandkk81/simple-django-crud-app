from audioop import reverse
from django.http import HttpResponse
from django.shortcuts import redirect, render

from members.models import Members

# Create your views here.

def index(request):
    mymembers = Members.objects.all().values()
    context = {
        'mymembers':mymembers
    }
    return render(request,'index.html',context)

def add(request):
    return render(request,'add.html',{})

def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    member = Members(firstname = x,lastname=y)
    member.save()
    return redirect('index')

def delete(request,id):
    member = Members.objects.get(id=id)
    member.delete()
    return redirect('index')

def update(request,id):
    mymember = Members.objects.get(id=id)
    context = {
        'mymember':mymember
    }
    return render(request,'update.html',context)

def updaterecord(request, id):
    first= request.POST['first']
    last = request.POST['last']
    member = Members.objects.get(id=id)
    member.firstname = first
    member.lastname = last
    member.save()
    return redirect('index')
    
