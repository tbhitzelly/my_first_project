from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from course.forms import GroupForm, StudentForm, BranchForm
from django.http import HttpResponse
from .models import Branch
from .models import Student
from .models import Group

def my_main_page(request):
  
    return render(request, 'course/my_page.html')
    
def branches_list(request):
    branches = Branch.objects.all()
    my_context = {'branches': branches}
    return render(request, 'course/branches_list.html', my_context)


def branch_edit(request, branch_id):
    branch = get_object_or_404(Branch, pk=branch_id)
    if request.method == "POST":
        form = BranchForm(request.POST, instance=branch)
        if form.is_valid():
            branch = form.save()
            return redirect('branch_detail', branch_id=branch.id)
    else:
        form = BranchForm(instance=branch)

    return render(request, 'course/branch_create.html', {'form': form})

def branch_create(request):
    if request.method == "POST":
        form = BranchForm(request.POST, request.FILES)
        if form.is_valid():
            branch = form.save()
            return redirect('branch_detail', branch_id=branch.id)
    else:
        form = BranchForm()

    return render(request, 'course/branch_create.html', {'form': form})

def branch_update(request, branch_id):
    branch = get_object_or_404(Branch, pk=branch_id)
    if request.method=="POST":
        form = BranchForm(request.POST)
        if form.is_valid():
            branch = form.save()
            return redirect('branch_detail', branch_id=branch.id)
    else:
        form = BranchForm(instance=branch)

    return render(request, 'course/branch_edit.html', {'form': form})   


def branch_detail(request, branch_id):
    branch = get_object_or_404(Branch, pk=branch_id)
    groups = Group.objects.filter(Branch=branch)
    context = {'branch': branch, 'groups': groups}
    return render(request, 'course/branch_detail.html', context=context)

def branch_delete(request, branch_id):
    query = Branch.objects.get(pk=branch_id)
    query.delete()
    return HttpResponseRedirect("/course/branches/")


def group_list(request):
    groups = Group.objects.all()
    my_context = {'groups': groups}
    return render(request, 'course/group_list.html', context=my_context)


def group_detail(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    students = Student.objects.filter(group=group)
    context = {'group': group, 'students': students}
    return render(request, 'course/group_detail.html', context=context)

def group_create(request):
    if request.method == "POST":
        form = GroupForm(request.POST, request.FILES)
        if form.is_valid():
            group = form.save()
            return redirect('group_detail', group_id=group.id)
    else:
        form = GroupForm()

    return render(request, 'course/group_create.html', {'form': form})

def group_edit(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    if request.method == "POST":
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            group = form.save()
            return redirect('group_detail', group_id=group.id)
    else:
        form = GroupForm(instance=group)

    return render(request, 'course/group_create.html', {'form': form})


def group_update(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    if request.method=="POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save()
            return redirect('group_detail', group_id=group.id)
    else:
        form = GroupForm(instance=group)

    return render(request, 'course/group_edit.html', {'form': form}) 

def group_delete(request, group_id):
    query = Group.objects.get(pk=group_id)
    query.delete()
    return HttpResponseRedirect("/course/groups/")



def student_list(request):
    students = Student.objects.all()
    my_context = {'students': students}
    return render(request, 'course/student_list.html', context=my_context)


def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    my_context = {'student': student}
    return render(request, 'course/student_detail.html', context=my_context)


def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save()
            return redirect('student_detail', student_id=student.id)
    else:
        form = StudentForm()

    return render(request, 'course/student_create.html', {'form': form})


def student_edit(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            return redirect('student_detail', student_id=student.id)
    else:
        form = StudentForm(instance=student)

    return render(request, 'course/student_create.html', {'form': form})


def student_update(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method=="POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('student_detail', student_id=student.id)
    else:
        form = StudentForm(instance=student)

    return render(request, 'course/student_edit.html', {'form': form}) 

def student_delete(request, student_id):
    query = Student.objects.get(pk=student_id)
    query.delete()
    return HttpResponseRedirect("/course/students/")