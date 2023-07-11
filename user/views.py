from django.shortcuts import render, redirect,get_object_or_404
from django.views import View
from .forms import CreateUserForm
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout, authenticate

# # Login View

def login_(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login_(request, user)
            messages.success(request, f'Welcome {username} ...')
            return redirect('ftx:home')
    else:
        messages.info(request, 'No account with username/password. Try Again!')
    form = Login_Form()
    return render(request, 'registration/login.html', {'form':form})
    
class Register_(View):

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect('/')
        
        # else process dispatch as it otherwise normally would
        return super(Register_, self).dispatch(request, *args, **kwargs)

    def register_(request):
        if request.method=='POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                print('Hello')
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account {username} sucessfully created...')
                return redirect('ftx:login')
            else:
                messages.error(request, 'Error')
        else:
            form = CreateUserForm
        return render(request, 'registration/register.html', {'register_form':form})

@login_required
def logout(request):
    logout(request)
    messages.info(request, 'Logged out ...')
    return redirect('user:login')