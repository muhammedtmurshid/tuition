from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


# Create your views here.
from teacher.forms import TeacherUserForm, TeacherForm


def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            messages.info(request, 'Login Success Fully')
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('admin_login')
    return render(request, 'admin_login.html')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def add_teacher(request):
    if request.method == 'POST':
        user_form = TeacherUserForm(request.POST)
        teacher_form = TeacherForm(request.POST)
        if user_form.is_valid() and teacher_form.is_valid():
            user = user_form.save()
            user.save()
            teacher = teacher_form.save(commit=False)
            teacher.user = user
            teacher.save()
            messages.info(request, 'Adding SuccessFull')
            return redirect('add_teacher')
        else:
            messages.error(request, 'Error Retry')
            return redirect('add_teacher')
    else:
        user_form = TeacherUserForm()
        teacher_form = TeacherForm()
    context = {
        'user_form': user_form,
        'teacher_form': teacher_form
    }
    return render(request, 'add_teacher.html', context)