from django.shortcuts import render,redirect
from .models import Article
from .forms import UserRegistrationForm,ArticleForm
from django.contrib import messages
from datetime import date
def home(request):
	return render(request,"index.html")
def register(request):
	if request.method=="POST":
		form=UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			reg_user=form.cleaned_data.get('username')
			messages.success(request,"Hello %s You Have successfully registered"%reg_user)
			return redirect('/blog/login')
	else:
		form=UserRegistrationForm()
	
	return render(request,"register.html",{"form":form})
def dashboard(request):
	return render(request,"dashboard.html")
def newarticle(request):
	if request.method=="POST":
		form=ArticleForm(request.POST)
		if form.is_valid():
			form1=form.save(commit=False)
			form1.user=request.user
			form1.articledate=date.today()
			form1.save()
			return redirect('/blog/newarticledone')
	else:
		form=ArticleForm()
	return render(request,"newarticle.html",{'form':form})
def newarticledone(request):
	return render(request,"newarticledone.html")
			# Create your views here.
