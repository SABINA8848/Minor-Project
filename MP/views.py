from django.shortcuts import render , redirect , HttpResponse
from django.contrib.auth.models import User
from django. contrib import messages
from .models import logins
from django.contrib.auth import logout

# Create your views here.
def index(request):
    try:
        if request.method =='POST':
            x = request.POST.get('username')
            y = request.POST.get('password')
            print(x,y)
            z=logins.objects.get(username=x)
            print(z.password)
            if y==z.password:
                return redirect('dashboard')
            else:
                return HttpResponse("Invalid Password")
    except:
        return HttpResponse("UNAUTHORIZED")
    return render(request,"index.html")

def register(request):
    try:
        if request.method =='POST':
            obj = logins()
            obj.username = request.POST.get('username')
            obj.fname = request.POST.get('fname')
            obj.lname = request.POST.get('lname')
            obj.password = request.POST.get('password')
            obj.email = request.POST.get('email')
            obj.save()
            print("Saved Successfully")
            return redirect('index')
    except:
        pass

    return render(request,"register.html")





    return render(request,"index.html")

def dashboard(request):
    return render(request,"Dashboard.html")

def notice(request):
    return render(request,"Notice.html")

def academic(request):
    return render(request,"Academic Calender.html")

def syllabus(request):
    return render(request,"Syllabus&OQ.html")

def staffs(request):
    return render(request,"Staffs.html")

def attendance(request):
    return render(request,"Attendance.html")

        
    

def logout_view(request):
    logout(request)
    return redirect('index')

def Register(request):
    if request.method =='POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User .objects.create_user(username, email, pass1)
        myuser. first_name = fname
        myuser. last_name = lname

        myuser.save()

        messages. success(request,"Your Account has been successfully created.")
        return redirect('index')

     
        




    
    return render(request,"Register.html")

