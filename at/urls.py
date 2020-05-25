from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='Home'),
    path('AboutUs/',views.AboutUs,name='AboutUs'),
    path('Contact/',views.Contact,name='Contact'),
    path('Register/',views.Register,name='Register'),
    path('Login/',views.Login,name='Login'),
    path('YourAppointments/',views.YourAppointments,name='YourAppointments'),
    path('InvoiceAndPayments/',views.InvoiceAndPayments,name='InvoiceAndPayments'),
    path('PatientProfile/',views.PatientProfile,name='PatientProfile'),
    path('MedicalHistory/',views.MedicalHistory,name='MedicalHistory'),
    path('Logout/',views.Logout,name='Logout'),
    path('DoctorProfile/',views.DoctorProfile,name='DoctorProfile'),
    path('Appointments/',views.Appointments,name='Appointments'),
    path('Prescriptions/',views.Prescriptions,name='Prescriptions'),
    path('CreatePrescription/',views.CreatePrescription,name='CreatePrescription'),
    path('ReceptionistDashboard/',views.ReceptionistDashboard,name='ReceptionistDashboard'),
    path('PatientProfileReceptionist/',views.PatientProfileReceptionist,name='PatientProfileReceptionist'),
    path('AppointmentFormReceptionist/',views.AppointmentFormReceptionist,name='AppointmentFormReceptionist'),
    path('HrDashboard/',views.HrDashboard,name='HrDashboard'),
    path('DoctorProfileHr/',views.DoctorProfileHr,name='DoctorProfileHr'),
    path('Accounting/',views.Accounting,name='Accounting'),
    ]







