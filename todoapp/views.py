from django.shortcuts import render,redirect
from django.contrib.auth import logout

# Create your views here.

from .models import AppUser,Task
from .forms import UserForm,TaskForm,LoginForm

def home(request):
    return render(request,'home.html')

def register(request):
    form=UserForm()
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'register.html',{'form':form})


def loginview(request):
    form=LoginForm()
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']

            try:
                user=AppUser.objects.get(
                    username=username,
                    password=password
                )
                request.session['user_id']=user.id
                request.session['username']=user.username
                return redirect('tasks')
            except AppUser.DoesNotExist:
                form.add_error(None, 'Invalid username or password')
    return render(request,'login.html',{'form':form})

def tasks(request):
    if 'user_id' not in request.session:
        return redirect('login')
    
    user_id=request.session['user_id']
    user=AppUser.objects.get(id=user_id)
    user_tasks=Task.objects.filter(user=user).order_by('-created_at')
    form=TaskForm()
    
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            task=form.save(commit=False)
            task.user=user
            task.save()
            return redirect('tasks')
    
    return render(request,'tasks.html',{'form':form,'tasks':user_tasks,'username':request.session['username']})

def logoutview(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    if 'username' in request.session:
        del request.session['username']
    return redirect('home')