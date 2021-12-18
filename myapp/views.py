from django.contrib.auth.models import User
from myapp.models import *
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect, render, HttpResponse, HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'index.html')
    #return HttpResponse("This is my app.")

def userlogin(request):
    return render(request, 'login.html')

def handlelogin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            if request.user.is_superuser:
                messages.success(request, "Welcome to Admin Dashboard!!")
                return redirect("/dashboard")
            else:
                messages.warning(request, "Successfully Loged In as User!!")
                return redirect("/events")
        else:
            messages.warning(request, "Invalid User")
            return redirect("/login")
    return HttpResponse("404 NOT FOUND")

def signup(request):
    return render(request, 'signup.html')


def handlesignup(request):
    if request.method=="POST":
        fname=request.POST['signupfname']
        lname=request.POST['signuplname']
        username=request.POST['signupusername']
        email=request.POST['signupemail']
        password=request.POST['signuppassword']
        password2=request.POST['signuppassword2']
        
        #check parameter
        if password!=password2:
            messages.error(request, "Password didn't match.")
            return HttpResponseRedirect('/signup')
        if User.objects.filter(username=username).first():
            messages.warning(request, "This username is already taken.")
            return HttpResponseRedirect('/signup')
        if User.objects.filter(email=email).first():
            messages.warning(request, "E-mail is already exist")
            return HttpResponseRedirect('/signup')

        #creating users.
        myuser=User.objects.create_user(username,email,password)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        return redirect('/login')
    else:
        return HttpResponse("404 error....")
    
def aboutus(request):
    return render(request, 'aboutus.html')

def events(request):
    return render(request, 'events.html')

def howitworks(request):
    return render(request, 'howitworks.html')

def dashboard(request):
    return render(request, 'dashboard/admindashboard.html')

def handlelogout(request):
    logout(request)
    messages.warning(request, "Successfully Logged Out")
    return redirect('/index')

def event(request):
    event=Event.objects.all()
    context={
        'events':event
    }
    return render(request, 'dashboard/event.html',context)

def profile(request):
    return render(request, 'dashboard/profile.html')

def addevent(request):
    if request.method=="POST":
        addeventname=request.POST['addeventname']
        eventcatagory=request.POST['eventcatagory']
        startdate=request.POST['startdate']
        enddate=request.POST['enddate']

        saveevent=Event(event_name=addeventname, event_catagory=eventcatagory, event_startdate=startdate, event_enddate=enddate)
        saveevent.save()
    messages.warning(request, "Event added successfully!!!")    
    return redirect('/event')

def deleteevent(request, event_id):
    event=Event.objects.get(pk=event_id)
    event.delete()

    messages.warning(request, "Event Deleted!!!")    
    return redirect('event')

def editevent(request, event_id):
    event=Event.objects.get(pk=event_id)
    
    return render(request,'editevent', {'event':'event'})
