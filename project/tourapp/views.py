
from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect,loader,HttpResponse
from.models import*
from.forms import *
from django.contrib.auth import login,logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .forms import UserRegistrationForm,UserLoginForm

from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate


from django.contrib.auth import authenticate
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods




# Create your views here.
def Index(request):
    
    return render(request, 'index.html') 

def search_packages(request):
    start_date = request.GET.get('startdate')
    end_date = request.GET.get('enddate')

    tour_packages = Pakage.objects.filter(start_date__lte=end_date, end_date__gte=start_date)

    return render(request, 'search.html', {'tour_packages': tour_packages})

def tour(request):
    packages=Pakage.objects.all()
    
    return render(request,'tourpackage.html',{'packages':packages})

def about(request):
    return render(request,"aboutus.html")
def main(request):
    if request.user.is_authenticated:
        username=request.user.username
        context={'username':username}
    else:
        context={}
    return render(request,"main.html")



def uslogout(request):
     logout(request)
     messages.success(request,'You have been successully logged out')
     
     return redirect('Index')


           
def vendor_logout(request):
     logout(request)
     messages.success(request,'logout successfully')
     return redirect('vendorlogin')

def editt(request,pk):
     package = get_object_or_404(Pakage,pk=pk)
     if request.method=='POST':
          form=PackageForm(request.POST,instance=package)
          if form.is_valid():
               form.save()
               return redirect('packagelist')
     else:
          form=PackageForm(instance=package)
          return render(request,'edit.html',{'form':form})


def delte(request,pk):
     package = get_object_or_404(Pakage,pk=pk)
     if request.method=='POST':
          package.delete()
          return redirect('packagelist')
     return render(request,'cnfirm.html',{'Pakage':package})





    




def packgedetail(request,pk):
   package=get_object_or_404(Pakage,pk=pk)
   
       
   return render(request,'packge_details.html',{'package':package})
   
     
   
   



def add_package(request):
    if request.method=='POST':
        form=PackageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('packagelist')
    else:

        form=PackageForm()
    return render(request,'addpackage.html',{'form':form})


def registerpage(request):
    return render(request,'register.html')

def useregister(request):
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            
            user.set_password(raw_password)
            user.save()
            first_name=form.cleaned_data.get('first_name')
            last_name=form.cleaned_data.get('last_name')
            username=form.cleaned_data.get('username')
            email=form.cleaned_data.get('email')
            profile=Profile.objects.create(user=user,first_name=first_name,last_name=last_name,username=username)
            return redirect('login')
    else:
        form=UserRegistrationForm()
    return render(request,'register.html',{'form':form})

def user_login(request):
  if request.method=='POST':
    form=UserLoginForm(data=request.POST)
    if form.is_valid():
       username=form.cleaned_data.get('username')
       password=form.cleaned_data.get('password')
       user=authenticate(username=username,password=password)
       if user is not None:
         login(request,user)
       return redirect('main')
  else:
      form=UserLoginForm()
  return render(request,'login.html',{'form':form})
            
def vendorregister(request):
    if request.method=="POST":
        vname=request.POST['vname']
        
        email=request.POST['email']
        
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        user=VendorRegister.objects.filter(Email=email)
        if user:
             message="User already exist"
             return render(request,"vendor_register.html",{'msg':message})
        else:
            if password == cpassword:
                newuser=VendorRegister.objects.create(Vendorname=vname,Email=email,Password=password,ConfirmPassword=cpassword)
                message="User register successfully"
                return render(request,"vendor_login.html",{'msg':message})
    else:
          
          return render(request,"vendor_register.html")
def vendorlogin(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        user=VendorRegister.objects.get(Email=email)
        if user:
            if user.Password==password:
                return render(request,"home.html")
    else:
          
        return render(request,"vendor_login.html")
def packagelist(request):
    package=Pakage.objects.all()
    return render(request,'packages.html',{'package':package})

    

def home(request):
    return render(request,'home.html')


def payment(request):
  return render(request,'payment.html')

@csrf_exempt
def payment_success_callback(request):
    
    
    return redirect('booking_confirmation')
def redirect_logged_in(view_func):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('book'))
        return view_func(request,*args,**kwargs)
    return wrapper

    
@login_required(login_url='/login/')
def book(request,package_id):
    package=Pakage.objects.get(pk=package_id)
    if request.method=='POST':
       form=BookingForm(request.POST,request.FILES)
       firstname=request.POST.get('firstname')
       lastname=request.POST.get('lastname')
       email=request.POST.get('email')
       phone=request.POST.get('phone')
       destination=request.POST.get('destination')
       seats=int(request.POST.get('seats'))
       if seats<=package.available_seats:
          booking=TravelBook(package=package,firstname=firstname,lastname=lastname,email=email,destination=destination,phone=phone,seats=seats)
          booking.save()
          package.available_seats-=seats
          package.save()
          if package.available_seats==0:
             return "Seats are full"
          else:
            return redirect('payment')
    else:
          form = BookingForm()  
    return render(request, 'book.html', {'form': form,'package':package})





 
    
    
def booking_confirmation(request):
    return render(request,'confirmation.html')

def bookinglist(request):
    data=TravelBook.objects.all()
    return render(request,'booklist.html',{'data':data})
    
    
     
        

    




    

            