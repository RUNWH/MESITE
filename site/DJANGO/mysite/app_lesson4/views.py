from django.shortcuts import render
from .models import Lesson4
#from django.http import HttpResponse

def index(request):
    advertisements=Advertisements.object.all()
    context={"advertisements":advertisements}
    return render(request,"index.html")

def top_sellers(request):
    return render(request, "top-sellers.html")

def advertisement_post(request):
    form=AdvertisementForm()
    context={"form":form}
    return render (request,'avertisement-post.html',context)