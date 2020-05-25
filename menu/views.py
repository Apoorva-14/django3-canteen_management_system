from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Breakfast
from .models import Lunch
from .models import Dinner
from .models import Special
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout, authenticate


def home(request):
    return render(request, 'menu/home.html')

#----------------------menu-------------------
def menulist(request):
    #Getting the objects from the model class
    breakfasts = Breakfast.objects.all()
    lunchs = Lunch.objects.all()
    dinners = Dinner.objects.all()
    specials = Special.objects.all()
    return render(request, 'menu/menulist.html', {'breakfasts':breakfasts,'lunchs':lunchs, 'dinners':dinners, 'specials':specials})


def confirm(request):
    #requesting the chosen qty from html file
    Bread_qty = request.GET.get('Bread')
    Poha_qty = request.GET.get('Poha')
    Idli_Sam_qty = request.GET.get('Idli_Sambhar')
    Sambhar_Dosa_qty = request.GET.get('Sambhar_Dosa')
    Pao_Bhaji_qty = request.GET.get('Pao_Bhaji')
    Paneer_Naan_qty = request.GET.get('Paneer_Naan')
    Dal_Mak_qty = request.GET.get('Dal_Makhni')
    Cholle_Bhat_qty = request.GET.get('Cholle_Bhature')
    Pizza_qty = request.GET.get('Special_Pizza')

    #requesting the item and mrp from our model
    Bread = Breakfast.objects.get(item='Bread')
    Poha = Breakfast.objects.get(item='Poha')
    Idli_Sambhar = Lunch.objects.get(item='Idli_Sambhar')
    Sambhar_Dosa = Lunch.objects.get(item='Sambhar_Dosa')
    Pao_Bhaji = Lunch.objects.get(item='Pao_Bhaji')
    Paneer_Naan = Dinner.objects.get(item='Paneer_Naan')
    Dal_Makhani = Dinner.objects.get(item='Dal_Makhni')
    Cholle_bhature = Dinner.objects.get(item='Cholle_Bhature')
    Pizza = Special.objects.get(item='Special_Pizza')

    #returning them in the form of list
    return render(request, 'menu/confirm.html',{'Bread':[Bread,Bread_qty],
    'Poha':[Poha,Poha_qty],
    'Idli_Sambhar':[Idli_Sambhar,Idli_Sam_qty],
    'Sambhar_Dosa':[Sambhar_Dosa,Sambhar_Dosa_qty],
    'Pao_Bhaji':[Pao_Bhaji,Pao_Bhaji_qty],
    'Paneer_Naan':[Paneer_Naan,Paneer_Naan_qty],
    'Dal_Makhni':[Dal_Makhani,Dal_Mak_qty],
    'Cholle_Bhature':[Cholle_bhature,Cholle_Bhat_qty],
    'Special_Pizza':[Pizza,Pizza_qty]})

#------------------------------------------------------


#-------------------------Auth--------------------------
def signupuser(request):
    if request.method == 'GET':
        return render(request, 'menu/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('menulist')
            except IntegrityError:
                return render(request, 'menu/signupuser.html', {'form':UserCreationForm(), 'error':'That username is already been taken,Please choose a new username'})
        else:
            return render(request, 'menu/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'menu/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'menu/loginuser.html', {'form':AuthenticationForm(), 'error':'User and password did not match'})
        else:
            login(request,user)
            return redirect('menulist')



def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def complete(request):
    return render(request, 'menu/complete.html')


def delete(request):
    return render(request, 'menu/delete.html')
