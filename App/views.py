from django.contrib.auth.models import User
from .models import Hospital, Doctors, Owner, Feature, Booking
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
import datetime


def home(request):
    return render(request, "App/home.html")


@login_required()
def dashboard(request):
    if (Hospital.objects.filter(user=request.user)):
        facilities = Feature.objects.filter(hospital=Hospital.objects.get(user=request.user))
        doctors = Doctors.objects.filter(hospital=Hospital.objects.get(user=request.user))
        if (request.method == "POST"):
            fid = request.POST.get("fid")
            did = request.POST.get("did")
            name = request.POST.get("name")
            total = request.POST.get("total")
            remaining = request.POST.get("remaining")
            date = datetime.datetime.now()
            hospital = Hospital.objects.get(user=request.user)

            if (request.POST.get("status") == "Save Facility"):
                facility = Feature(name=name, total=total, remaining=remaining, last_updated=date, hospital=hospital)
                facility.save()
            elif (request.POST.get("status") == "update fac"):
                Feature.objects.filter(id=fid).update(name=name, total=total, remaining=remaining, last_updated=date)
            elif (request.POST.get("status") == "delete fac"):
                Feature.objects.filter(id=fid).delete()
            elif (request.POST.get("status") == "Save Doctor"):
                name = request.POST.get("name")
                contact = request.POST.get("contact")
                email = request.POST.get("email2")
                speciality = request.POST.get("speciality")
                image = request.FILES.get("photo")
                print("Image",image)
                doctor = Doctors(name=name, email=email, contact=contact, speciality=speciality, hospital=hospital, image=image)
                doctor.save()
            elif (request.POST.get("status") == "update doc"):
                name = request.POST.get("name")
                contact = request.POST.get("contact")
                speciality = request.POST.get("speciality")
                Doctors.objects.filter(id=did).update(name=name, contact=contact, speciality=speciality)
            elif (request.POST.get("status") == "delete doc"):
                Doctors.objects.filter(id=did).delete()
        return render(request, "App/dashboard.html", {"facilities": facilities, "doctors": doctors})
    else:
        return redirect("/")


def results(request):
    if (request.method == "GET"):
        query = request.GET.get("query")
        if (query):
            hospitals = Hospital.objects.filter(name__contains=query)
        else:
            hospitals = Hospital.objects.all()
    return render(request, "App/results.html", {"hospitals": hospitals})


@login_required()
def dbookings(request):
    if (request.method == "POST"):
        status = request.POST.get("status")
        id = request.POST.get("id")
        if (status == "Mark Completed"):
            b = Booking.objects.get(id=id)
            remaining = Feature.objects.get(id = b.feature.id).remaining
            Feature.objects.filter(id = b.feature.id).update(remaining=remaining + 1,last_updated=datetime.datetime.now())
            Booking.objects.filter(id=id).update(status=False)
        else:

            b = Booking.objects.get(id=id)
            remaining = Feature.objects.get(id = b.feature.id).remaining
            Feature.objects.filter(id = b.feature.id).update(remaining=remaining - 1,last_updated=datetime.datetime.now())
            Booking.objects.filter(id=id).update(status=True)

    bookings = Booking.objects.filter(hospital=Hospital.objects.get(user=request.user))

    return render(request, "App/dbookings.html", {"bookings": bookings})


@login_required()
def bookbed(request, id):
    feature = Feature.objects.get(id=id)
    if request.method == "POST":
        booking = Booking.objects.filter(user=request.user, feature=feature, service_completed=False)
        if (booking):
            messages.error(request, 'You have already booked this facility!!', extra_tags="danger")
            pass
        else:
            booking = Booking(user=request.user, hospital=feature.hospital, feature=feature,
                              date=datetime.datetime.now(), status=True, service_completed=False)
            booking.save()
            remaining = feature.remaining
            Feature.objects.filter(id=id).update(remaining=remaining - 1,last_updated=datetime.datetime.now())
            messages.success(request, 'Congratulations! Your booking is confirmed')
    return render(request, "App/bookbed.html", {"feature": feature})


def hospital(request, id):
    hospital = Hospital.objects.get(id=id)
    doctors = Doctors.objects.filter(hospital=id)
    owner = Owner.objects.filter(hospital=id)
    features = Feature.objects.filter(hospital=id)
    return render(request, "App/hospitaldetail.html",
                  {"hospital": hospital, "doctors": doctors, "owner": owner, "features": features})


@login_required()
def bookings(request):
    bookings = Booking.objects.filter(user=request.user, status=True)
    completed = Booking.objects.filter(user=request.user, status=False)
    return render(request, "App/bookings.html", {"bookings": bookings, "completed": completed})


def hospitalDetails(request):
    hospital = Hospital.objects.filter(user=request.user)
    hospita = Hospital.objects.get(user=request.user)
    owners = Owner.objects.filter(hospital=hospita.id)
    print(owners)
    if (request.method == "POST"):
        status = request.POST.get("status")
        if (status == "Save"):
            name = request.POST.get("name")
            email = request.POST.get("email")
            phone1 = request.POST.get("phone1")
            phone2 = request.POST.get("phone2")
            address = request.POST.get("address")
            gmap = request.POST.get("gmap")

            Hospital.objects.filter(user=request.user).update(name=name, user=User.objects.get(id=request.user.id),
                                                              email=email, contact1=phone1,
                                                              contact2=phone2, hospitalAddress=address, mapUrl=gmap)
            messages.success(request, 'Success! Hospital Updated Successfully')
        elif (status == "Save Owner"):
            name = request.POST.get("name")
            email = request.POST.get("email")
            phone = request.POST.get("contact")
            image = request.FILES.get("image")

            owner = Owner(name=name, contact=phone, email=email, hospital=hospita, image=image)
            owner.save()
            messages.success(request, 'Success! Owner Saved Successfully')

        elif (status == "Update Owner"):
            name = request.POST.get("name")
            id = request.POST.get("id")
            email = request.POST.get("email")
            phone = request.POST.get("contact")


            Owner.objects.filter(id=id).update(name=name, email=email, hospital=hospita, contact=phone)
            messages.success(request, 'Success! Owner Updated Successfully')

        elif (status == "Delete Owner"):
            id = request.POST.get("id")
            Owner.objects.get(id=id).delete()
            messages.success(request, 'Success! Owner Deleted Successfully')



    return render(request, "App/hospitalDetails.html", {"hospital": hospital, "owner": owners})


def user_login(request):
    if (request.method == "POST"):
        name = request.POST.get("name")
        password = request.POST.get("password")
        uservalidity = authenticate(username=name, password=password)
        if (uservalidity is not None):
            print("User Authenticated")
            login(request, uservalidity)
            return redirect("/")
        else:
            print("Invalid Credentials")

    return render(request, "App/login.html")


@login_required()
def signup_as_hptl(request):
    if (request.method == "POST"):
        name = request.POST.get("name")
        email = request.POST.get("email2")
        phone1 = request.POST.get("phone1")
        phone2 = request.POST.get("phone2")
        address = request.POST.get("address")
        gmap = request.POST.get("gmap")
        image = request.FILES.get("display_photo")
        print("Image",image)
        hp = Hospital.objects.filter(user=request.user)
        print(hp)
        if (hp):
            messages.error(request, 'Sorry!, You Already Hold an Account', extra_tags="danger")
        else:
            hospital = Hospital(name=name, user=User.objects.get(id=request.user.id), email=email, contact1=phone1,
                                contact2=phone2, hospitalAddress=address, mapUrl=gmap, display_photo=image)
            hospital.save()
            messages.success(request, 'Congratulations! Hospital Registered Successfully')

    return render(request, "App/signup_as_hospital.html")


def signup(request):
    if (request.method == "POST"):
        name = request.POST.get("name")
        email = request.POST.get("email2")
        password = request.POST.get("password")
        status = request.POST.get("btnSignup")

        if (User.objects.filter(username=name) or User.objects.filter(email=email)):
            messages.error(request, 'Sorry!, You Already Hold an Account', extra_tags="danger")
        elif (User.objects.filter(email=email).first()):
            messages.error(request, 'Sorry!, This is Email is already taken', extra_tags="danger")
        else:
            user = User.objects.create_user(name, email, password)
            user.save()
            if (status == "Sign Up"):
                messages.success(request, 'Congratulations! Account Created Successfully')
                uservalidity = authenticate(username=name, password=password)
                if (uservalidity is not None):
                    print("User Authenticated")
                    login(request, uservalidity)
                    return redirect("/")
                else:
                    print("Invalid Credentials")
            else:
                uservalidity = authenticate(username=name, password=password)
                if (uservalidity is not None):
                    print("User Authenticated")
                    login(request, uservalidity)
                    return redirect("/signup_as_hptl")
                else:
                    print("Invalid Credentials")

    return render(request, "App/signup.html")


def user_logout(request):
    if (request.user.is_authenticated):
        logout(request)
        return redirect("/")
    else:
        return redirect("/")
