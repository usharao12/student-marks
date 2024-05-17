
from django.shortcuts import get_object_or_404, render
from result.models import Student1

def student_result(request,pk):
    student=get_object_or_404(Student1,pk=pk)
    context={
        'student':student,
    }
    return render(request,'student_result.html',context)
