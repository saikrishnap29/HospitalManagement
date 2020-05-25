from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
# Create your views here.
from.models import User
def Home(request):
    return render(request,'mainhome.html')

def AboutUs(request):
    return render(request,'AboutUs.html')

def Contact(request):
    return render(request,'Contact.html')

def Register(request):
    Register_form = RegisterForm()
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        register_as = request.POST['register_as']
        if password==confirm_password:
            form = User(firstname=firstname,lastname=lastname,username=username,
                        email=email,password=password,confirm_password=confirm_password,
                        register_as=register_as)
            form.save()
            return redirect('Home')
        else:
            messages.info(request, 'Password not Matched')
            return redirect('Register')
    return render(request, "register.html", {"Register_form": Register_form})

def Login(request):
    Login_form = LoginForm()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.get(username=username,password=password)
        if user is not None:
            usertype = user.register_as
            if usertype == "2":
                return render(request, "DoctorHome.html", )
            elif usertype == "3":
                return render(request, "HrHome.html", )
            elif usertype == "4":
                return render(request, "ReceptionistHome.html", )
            return render(request, "PatientHome.html",)
        else:
            messages.info(request,'Invalid Credentials')

    return render(request, "Login.html", {"Login_form": Login_form})

def YourAppointments(request):
    appointments = Appointment.objects.all()
    return render(request,'YourAppointments.html',{"appointments": appointments})

def InvoiceAndPayments(request):
    patients = Patient.objects.all()
    return render(request,'InvoiceAndPayments.html',{"patients": patients})

def PatientProfile(request):
    Patient_form = PatientFormPatient()
    if request.method == "POST":
        form = PatientFormPatient(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
    return render(request, "PatientProfilePatient.html", {"Patient_form": Patient_form})

def MedicalHistory(request):
    medicals = Prescription.objects.all()
    return render(request,'MedicalHistory.html',{"medicals": medicals})

def Logout(request):
    return render(request,'mainhome.html')

def DoctorProfile(request):
    Doctor_form = DoctorFormDoctor()
    if request.method == "POST":
        form = DoctorFormDoctor(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
    return render(request, "DoctorProfileDoctor.html", {"Doctor_form":Doctor_form})

def Appointments(request):
    appointments = Appointment.objects.all()
    for i in appointments:
        print(i)
    return render(request,'Appointments.html',{"appointments": appointments})

def Prescriptions(request):
    prescription = Prescription.objects.all()
    return render(request,'Prescriptions.html',{"prescription": prescription})

def CreatePrescription(request):
    Prescription_form = PrescriptionForm()
    if request.method == "POST":
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Prescriptions')
    return render(request, "CreatePrescription.html", {"Prescription_form":Prescription_form})

def ReceptionistDashboard(request):
    appointments = Appointment.objects.all()
    patients = Patient.objects.all()
    return render(request, 'ReceptionistDashboard.html', {"patients": patients,"appointments":appointments})

def PatientProfileReceptionist(request):
    patientreceptionist=PatientFormReceptionist()
    if request.method == "POST":
        form = PatientFormReceptionist(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ReceptionistDashboard')
    return render(request,'PatientProfileReceptionist.html',{"patientreceptionist":patientreceptionist})


def AppointmentFormReceptionist(request):
    AppointmentForms= AppointmentForm()
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ReceptionistDashboard')
    return render(request, 'CreateAppointment.html', {"AppointmentForms": AppointmentForms})

def HrDashboard(request):
    doctor=Doctor.objects.all()
    return render(request,'HrDashboard.html',{"doctor":doctor})

def DoctorProfileHr(request):
    doctorformhr=DoctorFormHr()
    if request.method == "POST":
        form = DoctorFormHr(request.POST)
        if form.is_valid():
            form.save()
            return redirect('HrDashboard')
    return render(request,'DoctorProfileHr.html',{"doctorformhr":doctorformhr})

def Accounting(request):
    patients=Patient.objects.all()
    return render(request,'Accounting.html',{"patients":patients})


