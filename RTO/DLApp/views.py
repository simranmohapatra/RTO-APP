from django.shortcuts import render,redirect
from DLApp.models import *
from .models import User
from django.contrib import messages
from django.contrib .auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/register')

def dl_insert(request):
    context = {}
    if request.method == "POST":
        datas = request.POST
        name = datas.get("dlname")
        dlno = datas.get("dlid")
        phno = datas.get("dlphno")
        address = datas.get("address")

        DLmodel.objects.create(dlname = name, dlid = dlno, dlphno = phno, address = address)

    dlMdata=DLmodel.objects.all()
    context ={"DL":dlMdata}

    return render(request,"index.html",context)
def delete(request,id):
    queryset = DLmodel.objects.get(id=id)
    queryset.delete()
    return redirect('/')
def update(request,id):
    queryset=DLmodel.objects.get(id=id)
    if request.method == "POST" :
        datas= request.POST
        name = datas.get("dlname")
        dlno = datas.get("dlid")
        phno = datas.get("dlphno")
        address = datas.get("address")

        queryset.dlname = name
        queryset.dlid = dlno
        queryset.dlphno = phno
        queryset.address = address
        queryset.save()
        # return redirect('/')
        return redirect('/#DATABASE')
    
    context={'upp':queryset}
    return render ( request,"update.html",context)

def loginpage(request):
    if request.method == "POST" :
        username = request.POST.get("username")
        password = request.POST.get("password")

        chack_username= User.objects.filter(username=username)
        if not chack_username.exists():
            messages.info(request,"Invalid Username.")
            return redirect('/login')
        
        user= authenticate(username=username,password=password)
        if user is None:
            messages.info(request,"Invalid password.")
            return redirect('/login')
        
        else:
            login(request,user)
            return redirect("/")
            # return render(request,"index.html")

    return render ( request,"loginpage.html")

def logoutpage(request):
    logout(request)
    return redirect("/login")

def register(request):
    if request.method == "POST" :
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request,"Username is alredy taken.")
            return redirect('/register')

        user=User.objects.create(first_name = first_name, last_name = last_name, username=username)

        user.set_password(password)
        user.save()
        messages.info(request,"account created.")
        return redirect('/register')
    

    return render ( request,"register.html")