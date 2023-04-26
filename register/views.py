from django.shortcuts import render,redirect
from . models import Student    

# Create your views here.


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        gender = request.POST.get('gender')
        data = Student(name=name, email=email, phone=phone, city=city,gender=gender)
        data.save()
        return render(request,'register/success.html',context={'data':data})

    else:
        return render(request, 'register/index.html')
    
def registrations(request,id=0):
    if request.method == 'POST':
        try:
            id=request.POST.get('id')
            data=Student.objects.get(id=id)
            return render(request,'register/registrations.html',context={'data':data,'single':True})
        except:
            return render(request,'register/404.html')

    else:
        data=Student.objects.all().order_by('-id')
        return render(request,'register/registrations.html',context={'data':data,'single':False})

def update(request,id):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        gender = request.POST.get('gender')
        data=Student.objects.get(id=id)
        
        data.name=name
        data.email=email
        data.phone=phone
        data.city=city
        data.gender=gender
        data.save()
        return redirect('register:registrations')
        

    else:    
        data=Student.objects.get(id=id)
        return render(request,'register/update.html',context={'data':data})

def delete(request,id):
    data=Student.objects.get(id=id)
    data.delete()
    return redirect('register:registrations')

