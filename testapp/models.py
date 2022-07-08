from django.db import models

# Create your models here.

class PersonalInformation(models.Model):
	surname=models.TextField(default="")
	firstname=models.TextField(default="")
	middlename=models.TextField(default="")
	dob=models.DateField(default="")
	gender=models.TextField(default="")
	vcat=models.TextField(default="")
	# age=models.TextField(default=None, blank=False)
	email=models.TextField(default="")
	phone=models.TextField(default="")
	

class meta:
	db_table = "table"

class VaccineInformation(models.Model):
	dsequence=models.TextField(default="")
	dolv=models.DateField(default="")
	brand1=models.TextField(default="")
	brand2=models.TextField(default="")
	brand3=models.TextField(default="")
	
class FacilityInformation(models.Model):
	fname=models.TextField(default="")
	fadd=models.TextField(default="")
	ftype=models.TextField(default="")

class RegisteredPersons(models.Model):
	person_info = models.ForeignKey(PersonalInformation, on_delete = models.CASCADE)
	vaccine = models.ForeignKey(VaccineInformation, on_delete = models.CASCADE)
	facility = models.ForeignKey(FacilityInformation, on_delete = models.CASCADE)
	wname=models.TextField(default="")
	wnum=models.TextField(default="")
	wtype=models.TextField(default="")


# class Health_worker(models.Model):
# 	wname = models.CharField(max_length=25)
# 	wlicense = models.IntegerField()
# 	wtype = models.CharField(max_length=25)

# class Facility(models.Model):
# 	fac_name = models.CharField(max_length=25)
# 	fac_city = models.CharField(max_length=25)
# 	fac_type = models.CharField(max_length=25)
# 	fac_add = models.CharField(max_length=25)
# 	vaccine = models.ManyToManyField(Vaccine)
# 	health_worker = models.ManyToManyField(Health_worker)

# class Appointment(models.Model):
# 	person_id = models.OneToOneField(Person, on_delete = models.CASCADE)
# 	facility = models.ForeignKey(Facility, on_delete = models.CASCADE)
# 	pref_time = models.TimeField(auto_now_add = False)
# 	pref_date = models.DateField()
# 	pref_loc = models.CharField(max_length=25)
# 	Dsequence = models.CharField(max_length=25)