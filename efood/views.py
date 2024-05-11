from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    title={
        'title':'Home'
    }
    return render(request,"index.html",title)
    

def accessories(request):
    title={
        'title':'Accessories'
    }
    return render(request,"accessories.html",title)
    

def category(request):
    title={
        'title':'Category'
    }
    return render(request,"category.html",title)

def shop(request):
    title={
        'title':'Shop'
    }
    return render(request,"shop.html",title)

def aboutUs(request):
    title={
        'title':'About Us'
    }
    return render(request,"aboutus.html",title)
    
    
    