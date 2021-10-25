from django.shortcuts import render, redirect
from .models import User,Purpose,Subscriber,Enquiry
import datetime
from django.core.files.storage import FileSystemStorage
from werkzeug.utils import secure_filename

# Create your views here.

def index(request):
    return render(request, 'crud/index.html')
	
def admin(request):
    return render(request, 'crud/admin.html')
	
def log(request):
    return render(request, 'crud/login.html')
	
	
def sign(request):
   return render(request, 'crud/signup.html')

def signup(request):
    p = User(username=request.POST['username'], password=request.POST['password'], mobile_number=request.POST['mobile_number'], email_id=request.POST['email_id'], gender=request.POST['gender'], address=request.POST['address'])
    p.save()
    return redirect('/')
	
def login(request):
    print("====================")
    user = None
    try:
      user = User.objects.get(username=request.POST['username'],password=request.POST['password'])
    except:
      print("ooo")
    print("====================")
    print(user)
    #print(user.username)
    if(user!=None):
            request.session['username'] = request.POST['username']
            if(request.POST['username'] == 'admin'):
                return render(request, 'crud/admin.html')
            else:
                return render(request, 'crud/index.html')
    else:
         return render(request, 'crud/invalid.html')
		 
def pup(request):
    return render(request, 'crud/enquire.html')
	
def purp(request):
    p = Purpose(name=request.POST['name'], age=request.POST['age'], tenth=request.POST['tenth'], twelth=request.POST['twelth'], graduate=request.POST['graduate'], stream=request.POST['stream'], phone=request.POST['phone'], visa_date_applied=request.POST['visa_date_applied'], visa_date_recieved=request.POST['visa_date_recieved'], purpose_of_visit=request.POST['purpose_of_visit'], college=request.POST['college'], country=request.POST['country'])
    p.save()
    return render(request, 'crud/admin.html')

def pview(request):
    purposes = Purpose.objects.all()
    context = {'purposes': purposes}
    return render(request, 'crud/pview.html', context)
    
def edit(request, id):
    purposes = Purpose.objects.get(id=id)
    context = {'purposes': purposes}
    return render(request, 'crud/edit.html', context)
    
def myupdate(request):
    p=Purpose.objects.get(name=request.POST['name'])
    p.name=request.POST['name']
    p.age=request.POST['age']
    p.tenth=request.POST['tenth']
    p.twelth=request.POST['twelth']
    p.graduate=request.POST['graduate']
    p.stream=request.POST['stream']
    p.phone=request.POST['phone']
    p.visa_date_applied=request.POST['visa_date_applied']
    p.visa_date_recieved=request.POST['visa_date_recieved']
    p.purpose_of_visit=request.POST['purpose_of_visit']
    p.college=request.POST['college']
    p.country=request.POST['country']
    p.save()
    return render(request, 'crud/admin.html')
	
def delete(request, id):
    p= Purpose.objects.get(id=id)
    p.delete()
    return render(request, 'crud/pview.html')
	
def daily(request):
    p = Subscriber(daily_alerts=request.POST['daily_alerts'])
    p.save()
    return render(request, 'crud/admin.html')
	
def dview(request):
    subscribers = Subscriber.objects.all()
    context ={'subscribers' : subscribers}
    return render(request, 'crud/dview.html', context)
	
def enq(request):
    return render(request, 'crud/enq.html')

def enquirer(request):
    p = Enquiry(fullname=request.POST['fullname'], contact=request.POST['contact'], visa_type=request.POST['visa_type'])
    p.save()
    return render(request, 'crud/index.html')

def fview(request):
    enquires = Enquiry.objects.all()
    context ={'enquires' : enquires}
    return render(request, 'crud/fview.html', context)	

	