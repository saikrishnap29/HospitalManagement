from django.db import models

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    username = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    REGISTER_AS_CHOICES = (
        ("1", "Patient"),
        ("2", "Doctor"),
        ("3", "HR"),
        ("4", "Receptionist"),
    )
    register_as = models.CharField(max_length=20, choices=REGISTER_AS_CHOICES, default='1')

    def __str__(self):
        return self.username

class Patient(models.Model):
    name=models.CharField(max_length=100)
    phone=models.IntegerField(blank=True)
    email=models.EmailField(blank=True)
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Others", "Others"))
    gender = models.CharField(max_length=20,choices=GENDER_CHOICES,default='1')
    age=models.IntegerField(blank=True)
    address=models.CharField(max_length=300)
    outstanding = models.IntegerField(blank=True)
    paid = models.IntegerField(blank=True)
    Blood_Group_CHOICES = (
        ('A+','A+ Type'),('B+','B+ Type'),('AB+','AB+ Type'),('O+','O+ Type'),('A-','A- Type'),('B-','B- Type'),('AB-','AB- Type'),('O-','O- Type') )
    blood_groop = models.CharField(max_length=40, choices=Blood_Group_CHOICES,default='1')
    med_reps = models.FileField(blank=True)
    case_paper = models.IntegerField(blank=True)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name=models.CharField(max_length=100)
    phone=models.IntegerField(blank=True)
    email=models.EmailField(blank=True)
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Others", "Others"))
    gender = models.CharField(max_length=20,choices=GENDER_CHOICES,default='1')
    age=models.IntegerField(blank=True)
    address=models.CharField(max_length=300)
    DEPARTMENT_CHOICES = (
        ("Neurologist", "Neurologist"),
        ("Psychiatrist", "Psychiatrist"),
        ("Anesthesiologist", "Anesthesiologist"),
        ("Dermatologist", "Dermatologist"),
        ("Cardiologist", "Cardiologist"),
        ("Orthopedist", "Orthopedist")
    )
    department=models.CharField(max_length=30, choices=DEPARTMENT_CHOICES, default='1')
    salary=models.IntegerField(blank=True)
    attendance=models.IntegerField(blank=True)
    STATUS_CHOICES = (
        ("Active", "Active"),
        ("In-Active", "In-Active"))
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='1')

    def __str__(self):
        return self.name

class Prescription(models.Model):
    date=models.DateField(auto_now_add=True)
    symptoms=models.CharField(max_length=100)
    prescription=models.CharField(max_length=300)
    patient=models.CharField(max_length=200)

    def __str__(self):
        return self.patient

class Appointment(models.Model):
    date=models.DateField()
    time=models.TimeField()
    doctor=models.CharField(max_length=200)
    patient=models.CharField(max_length=200)
    STATUS_CHOICES = (
        ("Pending", "Pending"),
        ("Completed", "Completed"))
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='1')

    def __str__(self):
        return self.patient


