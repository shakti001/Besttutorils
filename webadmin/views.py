from django.shortcuts import render
from webapp.models import Caurses ,Topic , Slider,general_setting ,Contact
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import   User , auth
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required

# Create your views here.

def is_admin(request):
    if request.user.is_superuser == False:
        return False

def login(request):
    if request.method == 'POST':
        username = request.POST['email']
          
        password = request.POST['password']          
        user = auth.authenticate(username=username , password=password)
        if user is None:
            messages.info(request, "invalid username or password ")
            return redirect('/ERP/')
        elif user.is_superuser == True:
            auth.login(request,user)
            return redirect('/ERP/index/')
        else:
            messages.info(request, "invalid username or password ")
            return redirect('/ERP/')
    else:
        gen = general_setting.objects.all()

        return render(request, 'login-page.html', {'gen':gen})


@login_required(login_url='/ERP/')
def index(request):
    gen = general_setting.objects.all()

    return render(request, 'home.html' , {'gen':gen})

@login_required(login_url='/ERP/')
def main(request):
    if request.method == 'POST':
        id  = request.POST['id']
        company_Logo = request.FILES['img']
        fs = FileSystemStorage()
        filename = fs.save(company_Logo.name,company_Logo)
        company_title = request.POST['title']
        company_email = request.POST['email']
        company_mobile = request.POST['mob']
        if company_Logo != 'None':
            c = general_setting.objects.filter(id=id).update(company_Logo=filename, company_title=company_title, company_email=company_email,company_mobile=company_mobile)
        else:
            c = general_setting.objects.filter(id=id).update( company_title=company_title, company_email=company_email,company_mobile=company_mobile)
            messages.info(request, "your details modified ")

            return redirect('/ERP/main/')
    else:
        u = general_setting.objects.filter(id=1)
        gen = general_setting.objects.all()

        return render(request,'main.html',{'u':u ,'gen':gen})

@login_required(login_url='/ERP/')
def course(request):
    caurse = Caurses.objects.all()
    return render(request, 'course.html' , {'caurse':caurse})

@login_required(login_url='/ERP/')
def add_course(request):
    if request.method == 'POST':
           
        image = request.POST['img']
        title = request.POST['title']
        about_title = request.POST['about_title']
        price = request.POST['price']
        caurse = Caurses(image=image,title=title,about_title=about_title,price=price).save()
        messages.info(request, " course is created ")
        return redirect('/ERP/course/')
    else:
        gen = general_setting.objects.all()

        return render(request, 'add-courses.html',{'gen':gen})

@login_required(login_url='/ERP/')
def edit_course(request , id):
    if request.method == 'POST':
        caurse_id= request.POST['caurse_id']
        title = request.POST['title']
        about_title = request.POST['about_title']
        image = request.POST['image']
      
        price = request.POST['price']
        caurse = Caurses.objects.filter(caurse_id=id).update(title=title,about_title=about_title,image=image,price=price)
        messages.info(request, " course is updated ")
        return redirect('/ERP/course/')
    else:
        gen = general_setting.objects.all()

        caurse = Caurses.objects.filter(caurse_id=id)
        return render(request, 'add-courses.html',{'caurse':caurse,'gen':gen})


@login_required(login_url='/ERP/')

def delete_course(request , id):
    instance = Caurses.objects.filter(caurse_id=id).delete()
    messages.info(request, " course is deleted ")

    return redirect('/ERP/course/')


@login_required(login_url='/ERP/')
def topic(request):
    tpc = Topic.objects.all()
    gen = general_setting.objects.all()

    return render(request,'topic.html' , {'tpc':tpc ,'gen':gen})

@login_required(login_url='/ERP/')
def add_topic(request):
    if request.method == 'POST':
        course = request.POST['caurse']
        name = request.POST['title']
        content = request.POST['content']

        tpc = Topic(name=name, content=content, caurse_id=course ).save()
        messages.info(request, "  created ")

        return redirect('/ERP/topic')
    
    else:
        c = Caurses.objects.all()
        cat = Caurses.objects.raw('SELECT * FROM webapp_Caurses as c  JOIN  webapp_Topic as t where c.caurse_id = t.caurse_id')
        gen = general_setting.objects.all()

        return render(request,'add-topic.html', {'c':c , 'cat':cat , 'gen':gen })

@login_required(login_url='/ERP/')
def edit_topic(request , id):
    if request.method == 'POST':
        topic_id = request.POST['topic_id']
        course = request.POST['caurse']
        name = request.POST['title']
        content = request.POST['content']
        tpc = Topic.objects.filter(topic_id=id).update(name=name, content=content, caurse_id=course)
        messages.info(request, "  updated ")

        return redirect('/ERP/topic/')
    
    else:
        c = Topic.objects.filter(topic_id=id)
        d = Caurses.objects.all()
        gen = general_setting.objects.all()

        # cat = Caurses.objects.filter(title = Topic.objects.filter(caurse_id=c))
        # cat = Caurses.objects.raw('SELECT * FROM webapp_Caurses   JOIN webapp_Topic  ON  webapp_Caurses.caurse_id =  webapp_Topic.caurse_id')
        return render(request,'add-topic.html', {'c':c  ,'d':d , 'edit':1 ,'gen':gen })


@login_required(login_url='/ERP/')
def del_topic(request , id):
   instance= Topic.objects.filter(topic_id=id).delete()
   messages.info(request, "  deleted ")

   return redirect('/ERP/topic/')  



@login_required(login_url='/ERP/')
def user(request):
    u = User.objects.all()
    return render(request , "user.html" , {'u':u })

def del_user(request , id):

   instance= User.objects.filter(id=id).delete()
   messages.info(request, "  deleted ")

   return redirect('/ERP/user/')  

@login_required(login_url='/ERP/')
def slider(request):
    se = Slider.objects.all()
    return render(request , "slider.html" , {'se':se })

def create_slider(request):
    if request.method == 'POST':
        # id = request.POST['id']
        company_Logo = request.FILES['img']
        fs = FileSystemStorage()
        filename = fs.save(company_Logo.name,company_Logo)        
        name = request.POST['title']
        se = Slider(image=filename, title=name).save()
        messages.info(request, "  created ")

        return redirect('/ERP/slider/')
    else:
        gen = general_setting.objects.all()

        return render(request , "add-slider.html" ,{'gen':gen})

def edit_slider(request , id):
    if request.method == 'POST':
        id = request.POST['id']
        company_Logo = request.FILES['img']
        fs = FileSystemStorage()
        filename = fs.save(company_Logo.name,company_Logo)        
        name = request.POST['title']
        se = Slider.objects.filter(id=id).update(image=filename, title=name)
        messages.info(request, "  updated ")

        return redirect('/ERP/slider/')
    else:
        gen = general_setting.objects.all()

        se = Slider.objects.filter(id=id)
        return render(request, 'add-slider.html', {'se':se ,'gen':gen})



def del_slider(request , id):
   instance= Slider.objects.filter(id=id).delete()
   messages.info(request, "  deleted ")
   return redirect('/ERP/slider/')  


@login_required(login_url='/ERP/')

def contact(request):
    contact = Contact.objects.all()
    gen = general_setting.objects.all()

    return render(request,'contactinfo.html',{'contact':contact,'gen':gen})



def del_contact(request , id):
   instance= Contact.objects.filter(id=id).delete()
   messages.info(request, " deleted ")
   return redirect('/ERP/contact/')  