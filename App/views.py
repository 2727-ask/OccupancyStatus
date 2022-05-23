from django.shortcuts import render
from .models import Hospital,Doctors,Owner,Feature
def home(request):
    return render(request,"App/home.html")



def results(request):
    if(request.method == "GET"):
        query = request.GET.get("query")
        hospitals = Hospital.objects.filter(name__contains=query)
    return render(request,"App/results.html",{"hospitals":hospitals})

def hospital(request,id):
    hospital = Hospital.objects.get(id=id)
    doctors = Doctors.objects.filter(hospital=id)
    owner = Owner.objects.filter(hospital=id)
    features = Feature.objects.filter(hospital=id)
    return render(request,"App/hospitaldetail.html",{"hospital":hospital,"doctors":doctors,"owner":owner,"features":features})