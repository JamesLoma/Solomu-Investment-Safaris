from django.shortcuts import redirect, render, HttpResponse
from datetime import datetime
from .models import Contact, register_table, updateemail
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import logout as django_logout

def index(request):
    return render(request, 'main/index.html')

def about (request):
    return render(request, 'main/about.html')

def contact(request):
    if request.POST.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, message=message, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent')

    return render(request, 'main/contact.html')

def travels(request):
    return render(request, 'main/travels.html')

def signin(request):
    if request.METHOD == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        #check if the user entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'main/index.html', {"success": "Logged in Successfully"})
        
        else:
            return render (request, 'auth/signin.html', {"message": "Enter the correct credentials"})
    
    return render(request, 'auth/signin.html')

def signup(request):
    if request.method == 'POST':
        fname = request.POST.get("firstname") 
        last = request.POST.get("lastname")
        un = request.POST.get("uname")
        pwd = request.POST.get("password")
        em = request.POST.get("email")
        con = request.POST.get("contact_number")

        usr = User.objects.create_user(un , em, pwd)
        usr.first_name = fname
        usr.last_name = last
        usr.save()

        reg = register_table(user=usr , contact_number=con)
        reg.save()

        return redirect('/signin' , {"status" : "{} Your Account is Created Successfully ".format(fname)}) 
        

    return render(request , 'authentication/signup.html')

def logout(request):
    django_logout(request)
    return redirect("/signin" , {"logsign" : " Logged Out Successfully"})

def profile(request):
    if request.user.is_authenticated:
        return render(request , 'main/profile.html')
    else:
        return redirect('/signin')

def error_404(request , exception):
    return render(request , 'main/404.html')

def blog(request):
    return render(request,'main/blog.html')

