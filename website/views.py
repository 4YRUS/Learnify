from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import sign_up
from .models import record2





def home(request):
	if request.user.is_authenticated:
		data = record2.objects.all()
		domains = set([item.domain for item in data])
		subdomains = set([item.subdomain for item in data])

		return render(request,'home.html',{'data':data, 'domains':domains,'subdomains':subdomains,"key":"ALL" ,"skey":"ALL"})
	else:
		return redirect('login')
def user_login(request):
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(request,username=username,password=password)
		if user:
			login(request,user)
			return redirect('home')
		return redirect('login')
	return render(request,'login.html',{})

def register(request):
	if request.method=='POST':
		form=sign_up(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,'User Created Succesfully...')
			return redirect('login')
		else:
			messages.success(request,'form invalid')
	else:
		form=sign_up()

	return render(request,'register.html',{'form':form})

def user_logout(request):
	logout(request)
	return redirect('login')

def display(request):
	objects = record2.objects.all()
	return render(request,'display.html',{'records':objects})
def search(request,word):
	data = record2.objects.all()
	domains = set([item.domain for item in data])
	subdomains = set([item.subdomain for item in data])
	data = [item for item in data if item.domain.lower() == word.lower() or word.lower() == "ALL".lower() or item.subdomain.lower()==word.lower()]
	return render(request,'home.html',{'data':data, 'domains':domains,'subdomains':subdomains,"key":word if word in domains else "ALL","skey":word if word in subdomains else "ALL"})

def search2(request,word):
	return search(request,word)