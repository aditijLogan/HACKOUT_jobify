from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User

# Create your views here.
def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        
        user = User.objects.filter(email = email, password=password).first()
        if user:
            res = HttpResponseRedirect('/ee')
            res.set_cookie('auth', email)
            return res
        else:
            return HttpResponseRedirect("/login")
    return render(request, "login.html")

def signup(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        name=request.POST["name"]
        confirmpassword=request.POST["confirmpassword"]

        if(password != confirmpassword):
            return HttpResponseRedirect("/signup")
        
        User.objects.create(name=name, email=email, password=password)
        return HttpResponseRedirect("/login")
    return render(request, "signup.html")
    
def home(request):
    return render(request, "index.html")
    
def ee(request):
    if not (request.COOKIES.get('auth')):
        return HttpResponseRedirect("/login")
    
    return render(request, "ee.html")