from django.shortcuts import render,redirect
from.models import Profile
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.


def home(req):

    user_id=req.session.get('user_id')
    if user_id is None:
        return redirect('login')
    user=User.objects.get(id=user_id)
    prof=Profile.objects.get(person=user)
    return render(req,'index.html',{'emp':prof})



def signin(req):
    if req.method=='POST':
        name=req.POST.get('name','')
        email=req.POST.get('email','')
        image=req.FILES['image']
        desi=req.POST.get('desi','')
        exp=req.POST.get('exp','')
        username=req.POST.get('username','')
        password=req.POST.get('password','')
        cpassword=req.POST.get('cpassword','')
        if  password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(req,'username alredy exists')
            elif User.objects.filter(email=email).exists():
                messages.info(req,'email alredy exists')
                return redirect('signin')
            else:
                user=User.objects.create_user(first_name=name,email=email,username=username,password=password)
                user.save()
                profi=Profile.objects.create(image=image,desi=desi,exp=exp,person=user)
                profi.save()
                
                return redirect('login')
        else:
            messages.info(req,'password doesnt match')
            return redirect('signin')
    return render(req,'signin.html')
def login(req):
    if req.method=='POST':
        username=req.POST.get('username','')
        password=req.POST.get('password','')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(req,user)
            req.session['user']=str(user)
            req.session['user_id'] = user.id
            return redirect('home')
        else:
            messages.info(req,"inavalid details")
            return redirect('login')
        
    return render(req,'login.html')
def logout(req):
    auth.logout(req)
    req.session.flush()
    return redirect('home')