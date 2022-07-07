from django.shortcuts import render, redirect
from django.views import View
from App.models import HospitalInformation, Feature, Doctors, Owner, HospitalImages, Booking
from django.contrib import messages
import datetime


# Create your views here.


class Dashboard(View):
    def get(self, request):
        info = HospitalInformation.objects.get(user=request.user)
        print(info)
        return render(request, "dashboard/dashboard.html", {'info': info})


class EditProfile(View):
    def get(self, request):
        info = HospitalInformation.objects.get(user=request.user)
        return render(request, "dashboard/edit-profile.html", {'info': info})

    def post(self, request):
        name = request.POST.get("name").lower()
        phone = request.POST.get("phone").lower()
        street = request.POST.get("street").lower()
        city = request.POST.get("city").lower()
        state = request.POST.get("state").lower()
        pin = request.POST.get("postal-code").lower()
        gmap = request.POST.get("gmap")

        HospitalInformation.objects.filter(user=request.user).update(name=name, phone=phone, street=street, city=city,
                                                                     state=state,
                                                                     pin=pin, gmap=gmap)
        info = HospitalInformation.objects.get(user=request.user)
        messages.success(request, 'Hospital profile updated successfully')
        # info = HospitalInformation(user=request.user, name=name, phone=phone, street=street, city=city, state=state,
        #                            pin=pin, gmap=gmap)
        # info.save()
        return render(request, "dashboard/edit-profile.html", {'info': info})


class FacilitiesView(View):
    def get(self, request):
        hospital = HospitalInformation.objects.get(user=request.user)
        features = Feature.objects.filter(hospital=hospital)
        return render(request, "dashboard/facilities.html", {"features": features})

    def post(self, request):
        hospital = HospitalInformation.objects.get(user=request.user)
        name = request.POST.get("name")
        total = request.POST.get("total")
        remaining = request.POST.get("remaining")

        print(name, total, remaining)
        feature = Feature(name=name, total=total, remaining=remaining, last_updated=datetime.datetime.now(),
                          hospital=hospital)
        feature.save()
        features = Feature.objects.filter(hospital=hospital)
        return render(request, "dashboard/facilities.html", {"features": features})


class FacilitiesUpdateView(View):
    def get(self, request, id):
        feature = Feature.objects.get(id=id)
        return render(request, "dashboard/edit_facility.html", {"feature": feature})

    def post(self, request, id):
        if (request.POST.get("action") == "Delete"):
            messages.success(request, 'Facility deleted successfully')
            Feature.objects.get(id=id).delete()
            return redirect("/dashboard/facilites")
        else:
            name = request.POST.get("name")
            total = request.POST.get("total")
            remaining = request.POST.get("remaining")
            Feature.objects.filter(id=id).update(name=name, total=total, remaining=remaining,
                                                 last_updated=datetime.datetime.now())
            feature = Feature.objects.get(id=id)
            messages.success(request, 'Facility updated successfully')
            return render(request, "dashboard/edit_facility.html", {"feature": feature})


class DoctorsView(View):
    def get(self, request):
        hospital = HospitalInformation.objects.get(user=request.user)
        doctors = Doctors.objects.filter(hospital=hospital)
        return render(request, "dashboard/doctors.html", {"doctors": doctors})

    def post(self, request):
        name = request.POST.get("name")
        contact = request.POST.get("contact")
        email = request.POST.get("email")
        speciality = request.POST.get("speciality")
        hospital = HospitalInformation.objects.get(user=request.user)
        image = request.FILES.get("image")

        doctor = Doctors(name=name, contact=contact, email=email, speciality=speciality, hospital=hospital, image=image)
        doctor.save()
        doctors = Doctors.objects.filter(hospital=hospital)

        messages.success(request, 'Doctor Added successfully')
        return render(request, "dashboard/doctors.html", {"doctors": doctors})


class DoctorsUpdateView(View):
    def get(self, request, id):
        doctor = Doctors.objects.get(id=id)
        return render(request, "dashboard/edit_doctor.html", {"feature": doctor})

    def post(self, request, id):
        if (request.POST.get("action") == "Delete"):
            messages.success(request, 'Doctor deleted successfully')
            Doctors.objects.get(id=id).delete()
            return redirect("/dashboard/doctors")
        else:
            name = request.POST.get("name")
            contact = request.POST.get("contact")
            email = request.POST.get("email")
            speciality = request.POST.get("speciality")
            hospital = HospitalInformation.objects.get(user=request.user)

            Doctors.objects.filter(id=id).update(name=name, contact=contact, email=email, speciality=speciality,
                                                 hospital=hospital)
            feature = Doctors.objects.get(id=id)
            messages.success(request, 'Doctor updated successfully')
            return render(request, "dashboard/edit_doctor.html", {"feature": feature})


class OwnersView(View):
    def get(self, request):
        hospital = HospitalInformation.objects.get(user=request.user)
        feature = Owner.objects.filter(hospital=hospital)
        return render(request, "dashboard/owners.html", {"feature": feature})

    def post(self, request):
        name = request.POST.get("name")
        contact = request.POST.get("contact")
        email = request.POST.get("email")
        hospital = HospitalInformation.objects.get(user=request.user)
        image = request.FILES.get("image")

        owner = Owner(name=name, contact=contact, email=email, hospital=hospital, image=image)
        owner.save()
        feature = Owner.objects.filter(hospital=hospital)

        messages.success(request, 'Owner Added successfully')
        return render(request, "dashboard/owners.html", {"feature": feature})


class OwnerUpdateView(View):
    def get(self, request, id):
        owner = Owner.objects.get(id=id)
        return render(request, "dashboard/edit_owner.html", {"feature": owner})

    def post(self, request, id):
        if (request.POST.get("action") == "Delete"):
            messages.success(request, 'Owner deleted successfully')
            Owner.objects.get(id=id).delete()
            return redirect("/dashboard/owners")
        else:
            name = request.POST.get("name")
            contact = request.POST.get("contact")
            email = request.POST.get("email")
            hospital = HospitalInformation.objects.get(user=request.user)

            Owner.objects.filter(id=id).update(name=name, contact=contact, email=email,
                                               hospital=hospital)
            feature = Owner.objects.get(id=id)
            messages.success(request, 'Owner updated successfully')
            return render(request, "dashboard/edit_owner.html", {"feature": feature})


class UploadImageView(View):
    def get(self, request):
        hospital = HospitalInformation.objects.get(user=request.user)
        images = HospitalImages.objects.filter(hospital=hospital)
        return render(request, "dashboard/images.html", {"images": images})

    def post(self, request):
        hospital = HospitalInformation.objects.get(user=request.user)
        images = HospitalImages.objects.filter(hospital=hospital)
        id = request.POST.get("id")
        action = request.POST.get("action")
        if(action == "delete"):
            print(id)
            HospitalImages.objects.get(id=id).delete()
            messages.error(request, 'You have already booked this facility!!', extra_tags="danger")
        else:
            img = request.FILES.get("image")
            image = HospitalImages(image=img, hospital=hospital)
            image.save()
            messages.success(request, 'Image Uploaded successfully')
        return render(request, "dashboard/images.html", {"images": images})


class ManageBookings(View):
    def get(self, request):
        hospital = HospitalInformation.objects.get(user=request.user)
        bookings = Booking.objects.filter(hospital=hospital)
        return render(request, "dashboard/manage_bookings.html",{"bookings":bookings})

    def post(self,request):
        status = request.POST.get("status")
        id = request.POST.get("id")

        if (status == "Mark Completed"):
            b = Booking.objects.get(id=id)
            remaining = Feature.objects.get(id=b.feature.id).remaining
            Feature.objects.filter(id=b.feature.id).update(remaining=remaining + 1,
                                                           last_updated=datetime.datetime.now())
            Booking.objects.filter(id=id).update(status=False)
        else:

            b = Booking.objects.get(id=id)
            remaining = Feature.objects.get(id=b.feature.id).remaining
            Feature.objects.filter(id=b.feature.id).update(remaining=remaining - 1,
                                                           last_updated=datetime.datetime.now())
            Booking.objects.filter(id=id).update(status=True)
        hospital = HospitalInformation.objects.get(user=request.user)
        bookings = Booking.objects.filter(hospital=hospital)
        return render(request, "dashboard/manage_bookings.html", {"bookings": bookings})




