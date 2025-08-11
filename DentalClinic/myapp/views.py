from django.shortcuts import render,redirect
from myapp.models import treatments,dentist,userreg,booking
import pyttsx3
from datetime import date
from django.db.models.functions import  Coalesce
from django.db.models import Sum
from django.db.models import Max,Value
from django.db.models import F
def showmyhomepage(request):
    trec=treatments.objects.all()
    drec=dentist.objects.all()
    return render(request,"homepage.html",{"trec":trec,"drec":drec})
def showadminpanel(request):
    return render(request,"adminpanel.html")
def adminaddtreatments(request):
    if request.method=="POST":
        tname=request.POST.get('tname')
        timage=request.FILES['timage']
        charge=request.POST.get('charge')
        ta=treatments(tname=tname,timage=timage,charge=charge)
        ta.save()
    return render(request,"adminaddtreatments.html")
def adminaddtreatmentlist(request):
    trec=treatments.objects.all()
    return render(request,"adminaddtreatmentlist.html",{"trec":trec})
def removetreatmentlist(request,id):
    treatments.objects.filter(id=id).delete()
    return redirect("/aatl/")
def edittreatmentlist(request,id):
    if request.method=="POST":
        tname=request.POST.get('tname')
        timage=request.FILES['timage']
        charge=request.POST.get('charge')
        treatments.objects.filter(id=id).update(tname=tname,timage=timage,charge=charge)
        return redirect("/aatl/")
    trec=treatments.objects.filter(id=id)
    for j in trec:
        tname=j.tname
        timage=j.timage
        charge=j.charge
    return render(request,"editaddtreatmentslist.html",{"tname":tname,"timage":timage,"charge":charge})
def dentistregform(request):
    if request.method == "POST":
        dname=request.POST.get('dname')
        em = request.POST.get('em')
        cno = request.POST.get('cno')
        photo = request.FILES['photo']
        gender = request.POST.get('gender')
        quali = request.POST.get('quali')

        uname = request.POST.get('uname')
        pword = request.POST.get('pword')
        da=dentist(dname=dname,em=em,cno=cno,quali=quali,photo=photo,gender=gender,uname=uname,pword=pword)
        da.save()
        return redirect("/shp/")
    return render(request,"dentistregistration.html")
def adminadddentistlist(request):
    drec=dentist.objects.filter(rights='ND')
    return render(request,"adminadddentistlist.html",{"drec":drec})

def adminapprovedentist(request,id):
    dentist.objects.filter(id=id).update(rights='D')
    return redirect("/aadl/")

def adminrejectdentist(request,id):
    dentist.objects.filter(id=id).update(rights='R')
    return redirect("/aadl/")
def userregform(request):
    if request.method == "POST":
        fname=request.POST.get('fname')
        em = request.POST.get('em')
        cno = request.POST.get('cno')
        gender = request.POST.get('gender')
        uname = request.POST.get('uname')
        pword = request.POST.get('pword')
        ua = userreg(fname=fname, em=em, cno=cno,gender=gender,uname=uname, pword=pword)
        ua.save()
        return redirect("/shp/")
    return render(request,"userregistration.html")
def showuserpage(request):
    trec=treatments.objects.all()
    return render(request,"userpagenew.html",{"trec":trec})
def treatmentdoctorspage(request,id):
    request.session['tid']=id
    trec=dentist.objects.filter(rights='D')
    return render(request,"treatmentdoctors.html",{"trec":trec})



def showbooking(request,id):
    bdate = date.today()
    max_bno = booking.objects.aggregate(max_bno=Coalesce(Max('bno'), Value(0)))['max_bno']
    bno = int(max_bno) + 1
    trec = treatments.objects.filter(id=request.session['tid'])
    for j in trec:
        tname = j.tname
        charge=j.charge

    patient=request.session['name']

    bdate=date.today()
    drec = dentist.objects.filter(id=id)
    for j in drec:
        dname = j.dname

    if request.method == "POST":
        rdate = request.POST.get('rdate')
        ba = booking(bno=bno,bdate=bdate, did=id,rdate=rdate,tname=tname, dname=dname,pid=request.session['id'], patient=patient,charge=charge)
        ba.save()
        return redirect("/sup/")

    return render(request,"Booking.html",{"bno":bno,"bdate":bdate,"dname":dname,"patient":patient,"tname":tname,"charge":charge})

def showuserbooking(request):
    rec=booking.objects.filter(pid=request.session['id'])
    return render(request,"userbookinglist.html",{"rec":rec})


def showadminuserbooking(request):
    rec=booking.objects.all()
    return render(request,"adminuserbookinglist.html",{"rec":rec})


def showdoctorpage(request):
    return render(request,"doctorpage.html")

def showdoctorNewbooking(request):
    rec = booking.objects.filter(did=request.session['id'], status='New Booking')
    return render(request, "doctorpageBooking.html", {"rec": rec})


def showdoctorBookingHistory(request):
    rec = booking.objects.filter(did=request.session['id'], status='Accept')
    return render(request, "doctorpageBookingH.html", {"rec": rec})

def adminapprovedoctor(request,id):
    booking.objects.filter(id=id).update(status='Accept')
    return redirect("/sdp/")

def adminrejectdoctor(request,id):
    booking.objects.filter(id=id).update(status='Reject')
    return redirect("/sdp/")

# Create your views here.
def loginpage(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        pword=request.POST.get('pword')
        found=0
        drec=dentist.objects.filter(uname=uname,pword=pword)
        if drec.exists():
            found=1
            for j in drec:
                id=j.id
                name=j.dname
                rights=j.rights
        if found==0:
            urec=userreg.objects.filter(uname=uname,pword=pword)
            if urec.exists():
                found=1
                for j in urec:
                    id=j.id
                    name=j.fname
                    rights=j.rights
        if found==0:
            msg="Sorry invalid user"
            engine=pyttsx3.init()
            engine.say(msg)
            engine.runAndWait()
        else:
            request.session['id']=id
            request.session['name'] = name
            request.session['uname'] = uname
            request.session['pword'] = pword
            request.session['rights'] = rights
            if rights=="A":
                return redirect('/sap/')
            elif rights=="D":
                return redirect('/sdp/')
            elif rights=="U":
                return redirect('/sup/')
    return render(request,"login.html")



def change(request):
    if request.method=="POST":
        t1=request.POST.get('t1')
        t2= request.POST.get('t2')
        t3= request.POST.get('t3')
        u=request.session['uname']
        p=request.session['pword']
        r=request.session['rights']
        if p ==t1:
            if t2 == t3:
                if r=="D":
                    dentist.objects.filter(uname=u,pword=p).update(pword=t2)
                else:
                    userreg.objects.filter(uname=u,pword=p).update(pword=t2)
                return redirect('/shp/')
            else:
                engine=pyttsx3.init()
                msg="sorry password missmatch"
                engine.say(msg)
                engine.runAndWait()
        else:
            engine = pyttsx3.init()
            msg = "invalid user"
            engine.say(msg)
            engine.runAndWait()
    return render(request,"changepass.html")
