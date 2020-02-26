from django.shortcuts import render,redirect
from .models import Article
from .forms import UserRegistrationForm,ArticleForm
from django.contrib import messages
from datetime import date
from django.contrib.auth.models import User
def home(request):
	user=request.GET.get("q")
	cont=0
	if user:
		try:
			User.objects.get(username=user)
			cont=1
		except:
			cont=2
	return render(request,"index.html",{"cont":cont,'search':user})
def register(request):
	if request.method=="POST":
		form=UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			reg_user=form.cleaned_data.get('username')
			messages.success(request,"Hello %s, You Have Successfully registered"%reg_user)
			return redirect('/blog/login')
	else:
		form=UserRegistrationForm()
	
	return render(request,"register.html",{"form":form})
def dashboard(request):
	return render(request,"dashboard.html")
def newarticle(request):
	if request.method=="POST":
		form=ArticleForm(request.POST,request.FILES)
		if form.is_valid():
			form1=form.save(commit=False)
			form1.user=request.user
			form1.articledate=date.today()
			form1.save()
			messages.success(request,"You Aritcle Has Been Posted Successfully")
			return redirect('/blog/dashboard')
	else:
		form=ArticleForm()
	return render(request,"newarticle.html",{'form':form})
def deletearticle(request,id):
	a=Article.objects.get(pk=id)
	a.delete()
	messages.success(request,"Article Has Been Successfully Deleted!")
	return redirect('/blog/dashboard')
def otherarticle(request,search):
	search=User.objects.get(username=search)
	return render(request,'otherarticle.html',{'search':search})
			# Create your views here.
