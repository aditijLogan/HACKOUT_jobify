from audioop import add
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Employee
from employer.models import Employer

# Create your views here.
def form(request):
    if not (request.COOKIES.get('auth')):
        return HttpResponseRedirect("/login")

        
    if request.method=='POST':
        email=request.POST["email"]
        name=request.POST["name"]
        age=request.POST["age"]
        phone=request.POST["phone"]
        gender=request.POST["gender"]
        education=request.POST["education"]
        skills=request.POST["job"]
        aadhar=request.POST["aadhar"]
        address=request.POST["address"]
    
        Employee.objects.create(
            email=email,
            name=name,
            age=age,
            phone=phone,
            skills=skills,
            education=education,
            address=address,
            gender=gender,
            aadhar=aadhar
        )
        return HttpResponseRedirect("table")
    
    return render(request, "employeeform.html")

def showData(request):
    if not (request.COOKIES.get('auth')):
        return HttpResponseRedirect("/login")
    
    if request.method=='POST':
        gender=request.POST["gender"]
        education=request.POST["education"]
        skills=request.POST["job"]

        emps = Employer.objects.filter(
            reqGender=gender,
            reqQualification=education,
            reqVacancy=skills
        ).all()

        return render(request, "tableemp.html", {"emps": emps})
    
    return render(request, "tableemp.html", {"emps": None})

