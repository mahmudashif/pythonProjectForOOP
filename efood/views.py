from django.http import HttpResponse
from django.shortcuts import render, redirect


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
    return render(request,"about_us.html",title)

def itemDescription(request):
    title={
        'title':'Item Description'
    }
    return render(request,'item_description.html',title)


def oderForm(request):
    title={
        'title':'Order Form'
    }
    return render(request,'form.html',title)
    

def successful(request):
    title={
        'title':'confirm'
    }
    return render(request,'success.html',title)