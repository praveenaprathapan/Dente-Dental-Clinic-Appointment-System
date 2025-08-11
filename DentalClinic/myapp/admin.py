from django.contrib import admin
from myapp.models import treatments,dentist,userreg,booking
class treatmentsadmin(admin.ModelAdmin):
    list_display = ('id','tname','timage','charge')
admin.site.register(treatments,treatmentsadmin)
class dentistadmin(admin.ModelAdmin):
    list_display = ('id','dname','em','cno','photo','quali','gender','uname','pword','rights')
admin.site.register(dentist,dentistadmin)
class userregadmin(admin.ModelAdmin):
    list_display = ('id', 'fname', 'em', 'cno', 'gender', 'uname', 'pword','rights')
admin.site.register(userreg,userregadmin)
class bookingadmin(admin.ModelAdmin):
    list_display = ('id', 'bno', 'bdate', 'rdate', 'dname', 'patient', 'tname','charge','status')
admin.site.register(booking,bookingadmin)
# Register your models here.
