from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from  .models import userprofail
import re





def register_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        

        if not User.objects.filter(username=username).exists():
            
            try:
                user_obj = User.objects.create(username=username)
                user_obj.password = make_password(password=password1)
                user_obj.save()

                messages.success(request, 'Your Account is Created. Now you can Login')
                return redirect('login_view')

            except Exception as e:
                print(e)

        else:
            messages.success(request, 'Try Another Username')
            return redirect('register_view')

    context = {}
    return render(request, 'profiles/register.html', context)







def login_view(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You Have Successfully Logged In.')


                return redirect('dashboard')

            else:
                messages.success(request, 'Type Correct Credentails')
                return redirect('register_view')

        except Exception as e:
            print(e)

    context = {}
    return render(request, 'profiles/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('login_view')










