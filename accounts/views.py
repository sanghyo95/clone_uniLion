from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth,messages
# Create your views here.
def signup(request):
    if request.method == "POST":
        if User.objects.filter(username=request.POST["email"]).exists():
                messages.add_message(request, messages.INFO, '이미 존재하는 아이디입니다.')
                return redirect('signup')
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["email"], password=request.POST["password1"])
            auth.login(request,user)
            return redirect('index')
        messages.add_message(request, messages.INFO,'비밀번호 , 비밀번호 확인 두 값이 다릅니다')
        return render(request, 'signup.html')

    return render(request,'signup.html')

def login(request):
    if request.method =="POST":
        username =request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        elif not (User.objects.filter(username=request.POST["email"]).exists()):
            messages.add_message(request, messages.INFO, '존재하지 않는 아이디입니다')
            return redirect('login')
        else:
            messages.add_message(request, messages.INFO, '비밀번호가 맞지 않습니다')
            return redirect('login')
    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')

def username_present(username):
    if User.objects.filter(username=username).exists():
        return True
    
    return False    