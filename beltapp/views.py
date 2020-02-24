from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.


def index(request):
    return render(request, "login.html")


def new(request):
    return render(request, 'index.html')


def create(request):
    print(request.POST)
    new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'],
    email=request.POST['email'], password=request.POST['password'], confirm=request.POST['confirm'])
    return redirect('/')


def welcome(request):
    if 'user' not in request.session:
        return redirect('/')
    else:
        context = {
            'user': User.objects.get(id=request.session['user'])
        }
    return render(request, 'login.html', context)


def registration(request):
    # basic_validator is from class UserManager
    #                               def basic_validaotor....
    errors = User.objects.basic_validator(request.POST)
    print(errors)
    if len(errors) > 0:
        # errors is a variable set at the top of this function
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
        # hashes pw and encrypts
    pwhash = bcrypt.hashpw(
        request.POST['password'].encode(), bcrypt.gensalt()).decode()
    # this is special for password due to bcrypt(pwhash is a variable)
    newUser = User.objects.create(
        first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pwhash)
    request.session['user'] = newUser.id
    return redirect('/welcome')
    print(pwhash)
    print(request.POST)


def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            print(request.POST)
        return redirect('/job')
    user = User.objects.get(email=request.POST['email'])
    request.session['user'] = user.id
    print(request.session['user'])
    print(User.objects.get(id=request.session['user']).first_name)
    return redirect('/job')


def logout(request):
    if 'user' not in request.session:
        return redirect('/')
    else:
        request.session.clear()
    return redirect('/')


def indexs(request):
    if 'user' not in request.session:
        return redirect('/')
    all_jobs = Job.objects.all()
    session_my_jobs= Job.objects.filter(user=request.session['user'])
    context = {
        'myjobs': session_my_jobs,
        'all_jobs': all_jobs,
        'user': User.objects.get(id=request.session['user'])
    }
    return render(request, 'index.html', context)


def news(request):
    context = {
        'job': Job.objects.all(),
        'user': User.objects.get(id=request.session['user'])
    }
    return render(request, 'make.html', context)


def creates(request):
    errors = Job.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('')
    else:
        Job.objects.create(title=request.POST['title'], desc=request.POST['desc'], location=request.POST['location'],add=False, user=User.objects.get(id=request.session['user']))
        print(Job)
    return redirect('/job')


def show(request, num):
    context = {
        'job': Job.objects.get(id=num)
    }
    return render(request, 'job/index.html', context)


def information(request, num):
    new_job = Job.objects.get(id=num)
    context = {
        'job': new_job,
        'user': User.objects.get(id=request.session['user'])
    }
    return render(request, 'view.html', context)


def edit(request, num):
    job = Job.objects.get(id=num)
    context = {
        'job': job,
        'user': User.objects.get(id=request.session['user'])
    }
    return render(request, 'edit.html', context)


def update(request, num):
    print(request.POST)
    errors = Job.objects.basic_validator(request.POST)
    print(errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('edit')
    else:
        print(request.POST)
        job = Job.objects.get(id=num)
        job.title = request.POST['title']
        job.desc = request.POST['desc']
        job.location = request.POST['location']
        job.save()
        return redirect('/job')


def destroy(request, num):
    print(request.POST)
    Job.objects.get(id=num).delete()
    return redirect('/job')


def add(request, num):
    job = Job.objects.get(id=num)
    job.granted = True
    job.save()
    return redirect('/job')
