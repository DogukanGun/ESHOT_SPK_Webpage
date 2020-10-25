from django.shortcuts import render,redirect
from .forms import LoginForm,RegisterForm
from .models import User
from django.contrib.auth.models import User as user
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login,logout
# Create your views here.
def login(request):
    form = LoginForm(request.POST)
    context = {
        "form":form,
        "id":2
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        try:
            main_user=User.objects.get(username=username)
            if not main_user.user_type=="waiting": 
                user = authenticate(request,username = username,password = password)  
                if user is None:
                    messages.info(request,"Kullanıcı Adı veya Parola Hatalı")
                    return render(request,"login.html",context) 
                messages.success(request,"Başarıyla Giriş Yaptınız")
                auth_login(request,user=user)
                context={
                    "id":0
                }
                return render(request,"search_engine.html",context)
            else:
                messages.info(request,"Giriş yapmadan önce kullanıcı izni almalısınız.")
        except:
            messages.info(request,"Veri tabanında oluşan bir hatadan kaynaklı giriş yapamıyorsunuz.")
        
        
    return render(request,"login.html",context)

def register(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            name=form.cleaned_data["name"]
            password = form.cleaned_data["password"] 
            user_type_="waiting"
            newUser = User(username=username,name=name,password=password,user_type=user_type_)
            newUser.save()
            userFromDjango=user(username=username)
            userFromDjango.set_password(password)
            userFromDjango.is_superuser=False 
            userFromDjango.save() 
            messages.info(request,"Başarıyla Kayıt Oldunuz...")
            return redirect("/authentication/login")
    else:
            form=RegisterForm()
    context = {
            "form" : form,
            "id":1
    } 
    return render(request,"login.html",context)


def main_page(request):
    my_user = request.user
    #If you want to know if the user is logged in
    is_user_logged = my_user.is_authenticated
    if is_user_logged is True:
        return render(request,"search_engine.html")
    else:
        return redirect("authentication/register")