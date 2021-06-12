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


def branch_detail(request, branch_id):
    branch = Branch.objects.get(id=branch_id)
    groups = Group.objects.filter(Branch=branch)
    context = {'branch': branch, 'groups': groups}
    return render(request, 'course/branch_detail.html', context=context)

def group_list(request):
    groups = Group.objects.all()
    my_context = {'groups': groups}
    return render(request, 'course/group_list.html', context=my_context)


def group_detail(request, group_id):
    group = Group.objects.get(id=group_id)
    students = Student.objects.filter(group=group)
    context = {'group': group, 'students': students}
    return render(request, 'course/group_detail.html', context=context)


def student_list(request):
    students = Student.objects.all()
    my_context = {'students': students}
    return render(request, 'course/student_list.html', context=my_context)


def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    my_context = {'student': student}
    return render(request, 'course/student_detail.html', context=my_context)