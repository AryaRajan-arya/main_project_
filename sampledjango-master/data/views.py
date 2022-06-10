from ast import Return
from ipaddress import ip_address
from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from numpy import roll
from .models import *
from .forms import *
import requests
import json
# Create your views here.
class Login(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            return redirect('index')
        else:
            form = AuthenticationForm()
            context = {'form':form}
            return render(request, 'login.html', context)

    def post(self,request):
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('index')
        else:
            context = {'form':form}
            return render(request, 'login.html', context)




class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class ListContact(View):
    def get(self,request):
        user = request.user
        if user.is_authenticated:
            contact = Contact.objects.filter(user=user)
            context = {'contact':contact,'user':user,'roll':roll}
            return render(request, 'list_contact.html', context)
        else:
            return redirect('login')

class AddContact(View):
    def get(self,request):
        user = request.user
        if user.is_authenticated:
            form = AddContactForm()
            context = {'form':form}
            return render(request, 'add_contact.html', context)
        else:
            return redirect('login')
    
    def post(self,request):
        form = AddContactForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect('index')

        
class EditContact(View):
    def get(self,request,id):
        user = request.user
        if user.is_authenticated:
            contact = Contact.objects.get(id=id)
            if contact.user == user:
                form = AddContactForm(instance=contact)
                context = {'form':form,'contact':contact}
                return render(request, 'edit_contact.html', context)
            else:
                return HttpResponse("You don't have permission to edit this contact")
        else:
            return redirect('login')

    def post(self,request,id):
        contact = Contact.objects.get(id=id)
        form = AddContactForm(request.POST,instance=contact)
        if form.is_valid():
            form.save()
            return redirect('index')


class DeleteContact(View):
    def get(self,request,id):
        user = request.user
        if user.is_authenticated:
            contact = Contact.objects.get(id=id)
            if contact.user == user:
                context = {'contact':contact}
                return render(request, 'delete_contact.html', context)
            else:
                return HttpResponse("You dont have permission to delete this contact")
        else:
            return redirect('login')

    def post(self,request,id):
        contact = Contact.objects.get(id=id)
        contact.delete()   
        return redirect('index')

class List(View):
    def get(self,request):
        form=List()
        context = {'form':form}
        return render(request,'list.html',context)
    
    def post(self,request):
        form = List(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

#LOCATION //////////////////
class SubmitLocation(View):
    def get(self,request):
        form=SubmitLocation()
        context = {'form':form}
        ip = requests.get('https://api.ipify.org?format=json')
        ip_data = json.loads(ip.text)
        #res = requests.get('http://ip-api.com/json/210.212.227.194')
        res = requests.get('http://ip-api.com/json/61.1.231.225')
        
        location_data_one = res.text
        location_data = json.loads(location_data_one)
        return render(request, 'SubmitLocation.html',{'data': location_data})
    
    def post(self,request):
        form = SubmitLocation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

class Var(View):
    def get(self,request):
        user = request.user
        if user.is_authenticated:
            contact = Contact.objects.filter(user=user)
            context = {'contact':contact,'user':user}
        ip = requests.get('https://api.ipify.org?format=json')
        ip_data = json.loads(ip.text)
        ip_address='61.1.231.225'
       #ip_address='210.212.227.194'
        res = requests.get('http://ip-api.com/json/ip_addres')
        location_data_one = res.text
        location_data = json.loads(location_data_one)
        if(ip_address=='61.1.231.225'):
            return render(request,'attendance.html',context)
        else:
            return render(request,'absent.html',context)

    def post(self,request):

        form =Var(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        




