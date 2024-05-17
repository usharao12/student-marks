from django.shortcuts import render

from result.models import Student1


def home(request):
    students=Student1.objects.all()
    context={
        'students':students,
    }
    return render(request,'home.html',context)