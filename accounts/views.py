from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User , auth

# Create your views here.

def login(request):

    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None and user.is_superuser==False:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect("login")
    
    else:
        return render(request,"my-account.html")

def login2(request):

    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None and user.is_superuser:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect("login2")
    
    else:
        return render(request,"my-account2.html")

def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method=="POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect("register")
            else:
                user = User.objects.create_user(username=username,password=password1,email=email)
                user.save()
        else:
            messages.info(request,'passwords not matching..')
            return redirect("register")
        
        return redirect('/')

    else:
        return render(request,"my-account.html")

def register2(request):
    if request.method=="POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect("register")
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,is_superuser=True)
                user.save()
        else:
            messages.info(request,'passwords not matching..')
            return redirect("register")
        
        return redirect('/')

    else:
        return render(request,"my-account2.html")