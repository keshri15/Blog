from django.shortcuts import render, HttpResponse
from .models import *  # Import the ContactTb model
from datetime import datetime
from django.contrib import messages
# Create your views here.

def home(request):
    Popular_BlogObj = Popular_Blog.objects.all()
    context = {'name':'Keshri','Popular_BlogObj':Popular_BlogObj}
    return render(request,'home.html',context)


def show_blog(request, pk):    
    showBlogObj = Popular_Blog.objects.get(pk = pk)
    return render(request, 'showBlog.html', {'showBlogObj':showBlogObj})

def about(request):
    return render(request,'about.html')

def allblogs(request):
    Regular_BlogObj = Regular_Blog.objects.all()
    context = {'name':'Keshri','Regular_BlogObj':Regular_BlogObj}
    return render(request,'allblogs.html',context)

def view_blog(request, pk):    
    viewBlogObj = Regular_Blog.objects.get(pk = pk)
    return render(request, 'viewBlog.html', {'viewBlogObj':viewBlogObj})

def contact(request):    
    if request.method == 'POST':
        name = request.POST['fullname']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        message = request.POST['message']
        
        # Create a ContactTb object and save it to the database
        contactObj = ContactTb(name=name, email=email, phone=phone,address=address, message=message)
        contactObj.save()
        messages.success(request, "Your message has been sent.")
        
    return render(request, 'contact.html')