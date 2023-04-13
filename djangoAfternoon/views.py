from django.shortcuts import render
from djangoAfternoon.form import EmpForm


def Home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about us.html")


def contact(request):
    return render(request, "contact us.html")


def myform(request):
    stu = EmpForm()
    return render(request, 'forms.html', {'form': stu})
