from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.views import View

class Index(View):
	def get(self,request,*args,**kwargs):
		return render(request,'customer/index.html')

class About(View):
	def get(self,request,*args,**kwargs):
		return render(request,'customer/about.html')

class Login(View):
	def get(self,request,*args,**kwargs):
		
		return render(request,'customer/login.html')


from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("Omkar")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index.html')
        else:
            # Handle invalid login (e.g., display an error message)
	    
            pass

    return render(request, 'customer/login.html')
