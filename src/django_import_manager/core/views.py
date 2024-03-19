import bcrypt

from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth.models import User

from core.forms import SignupForm
from core.models import SignUpKey


def login(request):
    return HttpResponse('Test')

def logout(request):
    auth_logout(request)
    return redirect(reverse('login'))

def index(request):
    print(request.user.is_authenticated)
    print(reverse('login'))
    if not request.user.is_authenticated:
        return redirect(reverse('login') + '?next=/')
    
    return render(request, 'core/index.html')

def user_management(request):
    users = User.objects.all()
    print(users)
    return render(request, 'auth/user-management.html', {'users': users})
    return HttpResponse("user management")

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        print(request.POST)
        username = request.POST['username']
        token = request.POST['token']
        # print("is form valid")
        # print(form.is_valid())
        # print("reeeee")
        if not form.is_valid():
            print("here!!!")
            print(form.errors)
            return render(request, 'core/signup.html', {'form': form, 'username': username, 'token': token})
        else:
            print("errors")
            print(form.errors)
        # return HttpResponse('Good')
    # if 'key' not in request.GET:
    #     if request.user.is_authenticated:
    #         return redirect('presto_index')
    #     else:
    #         return redirect('login')
    else:
        form = SignupForm()
        username = request.GET.get('username')
        token = request.GET.get('token')
    print("a1")
    try:
        signup_invite = SignUpKey.objects.get(username=username)
    except SignUpKey.DoesNotExist:
        if request.user.is_authenticated:
            return HttpResponse('aaa')
        else:
            return HttpResponse('bbb')
    print("b2")
    salt_encoded = bytes(signup_invite.salt, 'utf-8')

    token_encoded = bytes(token, 'utf-8')
    hashed_token = bcrypt.hashpw(token_encoded, salt_encoded)
    print("c3")
    if hashed_token.decode('utf-8') == signup_invite.hashed_token:
        print("GOODDDDD")
        if request.method == "GET":
            return render(request, 'core/signup.html', {'form': form, 'username': username, 'token': token})
        else:
            print(form.cleaned_data)
            print("TIME TO CREATE")
            User.objects.create(
                username=username,
                password=form.cleaned_data['password1']
            )
    return redirect('login')
