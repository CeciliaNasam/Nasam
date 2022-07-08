from django.shortcuts import render, redirect
#from django.http import HttpResponse
from .models import *

def home(request):
   return render(request, 'home.html')

def registedperson(request):
   registeredpersons = RegisteredPersons.objects.all()
   return render(request, 'registeredpersons.html', {'regpersons':registeredpersons})

def personal_info(request):
   if request.method == 'POST':
      userInfo = PersonalInformation.objects.create(surname=request.POST['surname'],
         firstname=request.POST['firstname'],
         middlename=request.POST['middlename'],
         dob=request.POST['dob'],
         gender=request.POST['gender'],
         vcat=request.POST['vcat'],
         email=request.POST['email'],
         phone=request.POST['phone'],
         )
      userInfo.save()

      return redirect(f'/index2/{userInfo.id}/')

   else:
      return render(request, 'personal_info_form.html')

def index2(request, user_id):
   userInfo = PersonalInformation.objects.get(id=user_id)

   if request.method == "POST":
      vaccine_info = VaccineInformation.objects.create(dsequence=request.POST['dsequence'],
         dolv=request.POST['dolv'],
         brand1=request.POST['brand1'],
         brand2=request.POST['brand2'],
         brand3=request.POST['brand3'],
         )
      vaccine_info.save()

      return redirect(f'/index3/{userInfo.id}/{vaccine_info.id}/')

   else:
      return render(request, 'index2.html')

def index3(request, user_id, vaccine_info_id):
   userInfo = PersonalInformation.objects.get(id=user_id)
   vaccine_info = VaccineInformation.objects.get(id=vaccine_info_id)


   if request.method == "POST":
      facilityinfo = FacilityInformation.objects.create(fname=request.POST['fname'],
         fadd=request.POST['fadd'],
         ftype=request.POST['ftype'],
         )
      facilityinfo.save()

      regperson_workerinfo = RegisteredPersons.objects.create(person_info=userInfo,
         vaccine=vaccine_info,
         facility = facilityinfo,
         wname=request.POST['wname'],
         wnum=request.POST['wnum'],
         wtype=request.POST['wtype'],)

      return redirect('/registedperson/')

   else:
      return render(request, 'index3.html')


def delete(request, reginfo_id):
   registered_info = RegisteredPersons.objects.get(id=reginfo_id)
   registered_info.delete()
   return redirect('/registedperson/')

def second(request):
   return render(request, 'second.html')

def second2(request):
   return render(request, 'second2.html')

def third(request):
   return render(request, 'third.html')

def pfizer(request):
   return render(request, 'pfizer.html')

def moderna(request):
   return render(request, 'moderna.html')

def sputnik(request):
   return render(request, 'sputnik.html')

def janssen(request):
   return render(request, 'janssen.html')

def astra(request):
   return render(request, 'astra.html')

def covaxin(request):
   return render(request, 'covaxin.html')

def coronavac(request):
   return render(request, 'coronavac.html')

def sinopharm(request):
   return render(request, 'sinopharm.html')

def reach(request):
   return render(request, 'reach.html')

def faq(request):
   return render(request, 'faq.html')

def Edit(request):
   return render(request, 'Edit.html')