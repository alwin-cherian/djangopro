from django.shortcuts import render, HttpResponse
from .models import post
from django.shortcuts import redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
from django.core.paginator import Paginator



# ob1 = post()
# ob2 = post()
# ob3 = post()
#
# ob1.head = 'GRACE PROPERTIES AND MARKETING'
# ob1.descr = 'plots @ mannuthy'
# ob1.date = '22/10/2018'
#
# ob2.head = 'GRACE PROPERTIES AND MARKETING'
# ob2.descr = 'plots @ vazhakkumpara'
# ob2.date = '12/08/2019'
#
# ob3.head = 'GRACE PROPERTIES AND MARKETING'
# ob3.descr = 'plots @ pattikad'
# ob3.date = '29/11/2019'
#
# objects=[ob1,ob2,ob3]


# def index(request):
#     return render(request, 'marketing-index.html',{'obj':objects})


def home(request):
    objects = post.objects.all()
    recents = post.objects.order_by('-date')[0:3]
    paginator = Paginator(objects,3)
    return render(request, 'marketing-index.html', {'ob': objects,'re':recents})



def logi(request):
    if request.method == 'POST':
        a = request.POST['username']
        b = request.POST['password']
        print(a, b)
        users = auth.authenticate(username=a, password=b)
        if users is not None:
            auth.login(request, users)
        else:
            messages.error(request,'PLEASE CHECK YOUR USERNAME OR PASSWORD')
            return redirect('film:loginn')
        return redirect('film:homie')
    return render(request, 'login.html')

def logo(request):
    auth.logout(request)
    return redirect('film:homie')

def reg(request):
    if request.method == 'POST':
        a = request.POST['first name']
        c = request.POST['Username']
        d = request.POST['Password']
        e = request.POST['last name']
        f = request.POST['Email']
        if d == e:
            if User.objects.filter(username=c).exists():
                messages.error(request,'username used')
                return redirect('film:register')
            elif User.objects.filter(email=f).exists():
                messages.error(request,'email used')
                return redirect('film:register')
            else:
                v=User.objects.create_user(first_name=a, username=c, password=d, last_name=e, email=f, is_superuser=False, is_staff=True)
                v.save()
                auth.login(request,v)
                return redirect('film:homie')
        else:
            messages.error(request,'PASSWORD NOT CORRECT')
            return redirect('film:register')
    return render(request,'register.html')


