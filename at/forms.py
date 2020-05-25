from django import forms
from.models import *
from django.forms import ChoiceField

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = "__all__"

    register_as = ChoiceField(choices=[ ("1", "Patient"),
        ("2", "Doctor")])

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']

class PatientFormPatient(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = ['outstanding','paid']

class PatientFormReceptionist(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"

class DoctorFormDoctor(forms.ModelForm):
    class Meta:
        model = Doctor
        exclude = ['salary','attendance','status']

class DoctorFormHr(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = "__all__"

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = "__all__"