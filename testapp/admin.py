from django.contrib import admin
from .models import * 

admin.site.register([PersonalInformation, VaccineInformation, FacilityInformation
	, RegisteredPersons])
# Register your models here.
