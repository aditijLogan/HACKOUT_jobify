from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Employer
from employee.models import Employee

# Create your views here.
def form(request):
    if not (request.COOKIES.get('auth')):
        return HttpResponseRedirect("/login")

    if request.method=='POST':
        email=request.POST['email']
        name=request.POST["name"]
        reqGender=request.POST["gender"]
        reqQualification=request.POST["education"]
        reqVacancy=request.POST["job"]
        phone=request.POST["phone"]
        WorkAddress=request.POST["WorkAddress"]
        age=request.POST["age"]
    
        Employer.objects.create(
            email=email,
            name=name,
            age=age,
            reqGender=reqGender,
            reqQualification=reqQualification,
            reqVacancy=reqVacancy,
            phone=phone,
            WorkAddress=WorkAddress
        )
        return HttpResponseRedirect("table")
    
    return render(request, "employerform.html")

def showData(request):
    if not (request.COOKIES.get('auth')):
        return HttpResponseRedirect("/login")
    
    if request.method=='POST':
        reqGender=request.POST["gender"]
        reqQualification=request.POST["education"]
        reqVacancy=request.POST["job"]

        emps = Employee.objects.filter(
            education=reqQualification,
            gender=reqGender,
            skills=reqVacancy
        ).all()

        return render(request, "table", {"emps": emps})
    
    return render(request, "tableempr.html", {"emps": None})

