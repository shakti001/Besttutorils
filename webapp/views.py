from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

from django import forms
from .forms import RegisterForm
from .models import Slider , Tutorial ,Caurses,footer_discription,Contact,email_templates,Topic,general_setting
# Create your views here.
def index(request):
    slider = Slider.objects.all()
    tut = Tutorial.objects.all()
    cau = Caurses.objects.all()
    gen = general_setting.objects.all()
    foot = footer_discription.objects.all()
    return render(request, 'index.html', {'slider':slider ,'tut':tut,'cau':cau, 'foot':foot , 'gen':gen})

def contact(request):
    if request.method =='POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        mob = request.POST['mob']
        email = request.POST['email']
        message = request.POST['mess']
        con = Contact(firstname=firstname,lastname=lastname,mob=mob,email=email,message=message).save()
        messages.info(request,  " your message has been send ")
        # em = email_templates.objects.get(id=2)
        # send_to = [email]
        # subject = em.sub.replace('{username}',sub)
        # content = em.content.replace('{username}',sub)
        # sendMail(subject, content, send_to)
        return redirect('/contact/')

    else:

        cau = Caurses.objects.all()
        gen = general_setting.objects.all()

        return render(request,'contact.html',{'cau':cau ,'gen':gen})

def register(request):
  
    if request.method == 'POST':
        form  = RegisterForm(request.POST)
        
        
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            re_password = form.cleaned_data.get('re_password')
           
            
            if password == re_password :
                if User.objects.filter(username=name).exists():
                    messages.info(request , 'username Allready taken')
                    return redirect('/register/')
                if User.objects.filter(email=email).exists():
                    messages.info(request , 'email Allready taken')
                    return redirect('/register/')
                else:
                    details = User.objects.create_user(username=name, email=email,   password=password,is_staff=False, is_active=True, is_superuser=False, )
                    details.save()
                    messages.success(request, 'sign up details updated.')
                    em = email_templates.objects.get(id=1)
                    send_to = [email]
                    subject = em.sub.replace('{username}', name)
                    content = em.content.replace('{username}', name)
                    sendMail(subject, content, send_to)
                    return redirect('/login/' )
            else:
                messages.info(request , 'password does not match')
                return redirect('/register/')

    else:
        fr = RegisterForm()
        cau =Caurses.objects.all()
        gen = general_setting.objects.all()

        return render(request,'register.html',{'fr':fr ,'cau':cau ,'gen':gen})
        
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username , password=password )
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, "invalid username or password ")
            return redirect('/login/')
    else:
        cau = Caurses.objects.all()
        gen = general_setting.objects.all()

        return render(request, 'login.html',{'cau':cau ,'gen':gen})

def logout(request):
    auth.logout(request)
    return redirect('/')

def sendMail(subject, message, recipient):
    send_mail(
        subject = subject,
        message = message,
        from_email = 'test@cashbackoffers.win',
        recipient_list = recipient
    )
    return None

def tutorial(request):
    tut = Tutorial.objects.all()
    gen = general_setting.objects.all()

    return render(request,'tutorial.html',{'tut':tut,'gen':gen})

def caurse(request):
    cau = Caurses.objects.all()
    gen = general_setting.objects.all()

    return render(request,'courses.html',{'cau':cau ,'gen':gen})

def single_caurse(request , id):
    gen = general_setting.objects.all()

    cau = Caurses.objects.filter(caurse_id=id)
    top = Topic.objects.raw('SELECT topic_id,name FROM webapp_Topic WHERE caurse_id='+str(id))

    return render(request,'course-single.html', {'cau':cau, 'top':top ,'gen':gen})

@login_required(login_url='/login/')
def topic_read(request , id ):
    cau = Caurses.objects.all()
    gen = general_setting.objects.all()

    tpread = Topic.objects.raw('SELECT topic_id,content FROM webapp_Topic WHERE topic_id='+str(id))

    return render(request , 'topic_read.html', {'cau':cau, 'tpread': tpread ,'gen':gen})

