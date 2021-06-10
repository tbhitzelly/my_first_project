from django.shortcuts import render
from django.http import HttpResponse
from .models import Branch
from .models import Student
from .models import Group

def my_main_page(request):
    my_context = {'name': 'itc',
    'my_list': [1,2,3,4,5]
    }
    return render(request, 'course/my_page.html', context=my_context)
    
def branches_list(request):
    branches = Branch.objects.all()
    my_context = {'branches': branches}
    return render(request, 'course/branches_list.html', my_context)

def student_list(request):
    student = Student.objects.all()
    my_context = {'student': student}
    return render(request, 'course/student_list.html', my_context)

def group_list(request):
    groups = Group.objects.all()
    my_context = {'groups': groups}
    return render(request, 'course/group_list.html', my_context)