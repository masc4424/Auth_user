from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


def admin_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')


@login_required(login_url='admin_login')
@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard(request):
    emp = User.objects.all()
    context = {'emp': emp}
    return render(request, 'admin_dashboard.html', context)


@login_required(login_url='admin_login')
@user_passes_test(lambda u: u.is_superuser)
def add(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        # Encrypt the password
        encrypted_password = make_password(password)

        emp = User(
            first_name=fname,
            last_name=lname,
            username=username,
            email=email,
            password=encrypted_password
        )
        emp.save()
        return redirect('admin_dashboard')
    return render(request, 'admin_dashboard.html')


@login_required(login_url='admin_login')
@user_passes_test(lambda u: u.is_superuser)
def edit(request):
    emp = User.objects.all()
    context = {'emp': emp}
    return render(request, 'admin_dashboard.html', context)


@login_required(login_url='admin_login')
@user_passes_test(lambda u: u.is_superuser)
def update(request, id):
    emp = User.objects.get(id=id)
    if request.method == "POST":
        emp.first_name = request.POST.get('fname')
        emp.last_name = request.POST.get('lname')
        emp.username = request.POST.get('username')
        emp.email = request.POST.get('email')
        emp.save()
        return redirect('admin_dashboard')
    context = {'emp': emp}
    return render(request, 'update.html', context)


@login_required(login_url='admin_login')
@user_passes_test(lambda u: u.is_superuser)
def delete(request, id):
    emp = User.objects.filter(id=id)
    emp.delete()
    context = {
        'emp': emp,
    }
    return redirect('admin_dashboard')


def admin_logout_view(request):
    logout(request)
    return redirect('admin_login')
