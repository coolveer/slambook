from django.shortcuts import render
from.models import Fdetail
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .forms import LoginForm,SignupForm,Slam_detail
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
     
    form = LoginForm()
    context= {'form':form}
    return render(request,'index.html',context)
def login_pro(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            pkey=request.user.id
            return redirect('home/{}'.format(pkey))
        else:
            return redirect('/')
def signup_view(request):
    form = SignupForm()
    context= {'form':form}
    return render(request,'signup.html',context)
def signup_pro(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            user = User.objects.create_user(username, email, password1)
            user.first_name = fname
            user.save()
            send_mail(
                'Welcome {} we are pleased to have you here at slambook.'.format(fname),
                'hey {} wlcome to our website. You have been added you to our mailing list and you will get notified when ever your friend will fill your slambook.  Thanks for joining us from The Slam Book team  '.format(fname),
                'coolveer.singh110@gmail.com',
                ['{}'.format(email)],
                fail_silently=False,
                )
            
            
            return redirect('/')
def home(request,pk):
    pkey=pk
    firstn=request.user.first_name
    #db=Fdetail.objects.all().filter(fkey="{}".format(pkey))
    db=Fdetail.objects.filter(fkey='{}'.format(pkey))
    context={'firstn':firstn,'db':db}
    return render(request,'home.html',context)
def detail_slam(request,pk,fname):
    fname=fname
    pk=pk
    form=Slam_detail()
    context={'form':form,'fname':fname,'pk':pk}
    return render(request,'slambook.html',context)
def logout_view(request):
    logout(request)
    return redirect('/')

def process_slam(request,pk):
    pk=pk
    # from here we are getting the elements 
    if request.method=='POST':
        form = Slam_detail(request.POST, request.FILES)
        if form.is_valid():
            profile = Fdetail()
            profile.pic = form.cleaned_data["pic"]
                
            profile.name=request.POST['name']
            profile.home=form.cleaned_data['home']
            profile.pno=form.cleaned_data['pno']
            profile.born=form.cleaned_data['born']
            profile.become=form.cleaned_data['become']
            profile.dream=form.cleaned_data['dream']
            profile.sport=form.cleaned_data['sport']
            profile.relation=form.cleaned_data['relation']
            profile.look=form.cleaned_data['look']
            profile.eat=form.cleaned_data['eat']
            profile.movies=form.cleaned_data['movies']
            profile.dislike=form.cleaned_data['dislike']
            profile.crazy=form.cleaned_data['crazy']
            profile.moment=form.cleaned_data['moment']
            profile.holiday=form.cleaned_data['holiday']
            profile.friendship=form.cleaned_data['friendship']
            profile.withyou=form.cleaned_data['withyou']
            profile.hobbies=form.cleaned_data['hobbies']
            profile.truth=form.cleaned_data['truth']
            profile.you=form.cleaned_data['you']
            profile.love=form.cleaned_data['love']
            profile.date=form.cleaned_data['date']
            profile.fkey='{}'.format(pk)
            profile.save()
            name=request.POST['name']
            db=User.objects.get(pk=pk)
            
            send_mail(
                'Slambook Notification',
                'This is just to let you know your friend {} just filled your slambook  '.format(name),
                'coolveer.singh110@gmail.com',
                ['{}'.format(db.email)],
                fail_silently=False,
                )
            if request.user.is_authenticated:
                return redirect('home',pk=pk )
            else:
            #when the user is not signuped then
                return redirect('signup')
        #pushing the data in the database 
            
            
def detail(request,pk):
    pkey=pk
    db=Fdetail.objects.filter(pk='{}'.format(pkey))
    context={'db':db}
    return render(request,'detail.html',context)
        
        
            
    
            
            
