from django.urls import path
from . import views
urlpatterns=[
    path('',views.showmyhomepage),
    path('shp/',views.showmyhomepage),
    path('sap/',views.showadminpanel),

    path('aat/',views.adminaddtreatments),
    path('aatl/',views.adminaddtreatmentlist),
    path('del/<int:id>/',views.removetreatmentlist),
    path('edit/<int:id>/',views.edittreatmentlist),
    path('dreg/',views.dentistregform),
    path('aadl/',views.adminadddentistlist),
    path('reject/<int:id>/',views.adminrejectdentist),
    path('approve/<int:id>/', views.adminapprovedentist),
    path('ur/',views.userregform),
    path('sup/',views.showuserpage),
    path('tdp/<int:id>/',views.treatmentdoctorspage),
    path('sb/<int:id>/',views.showbooking),
    path('lg/',views.loginpage),
    path('sbl/',views.showuserbooking),
    path('asbl/',views.showadminuserbooking),
    path('sdp/',views.showdoctorpage),
    path('appro/<int:id>/',views.adminapprovedoctor),
    path('rejt/<int:id>/',views.adminrejectdoctor),
    path('sdnb/',views.showdoctorNewbooking),
    path('sdbH/',views.showdoctorBookingHistory),
    path('cpw/',views.change),

]