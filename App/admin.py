from django.contrib import admin
from .models import Doctors,Hospital,Owner,Feature,UserDetails,Booking
# Register your models here.
admin.site.register(Doctors)
admin.site.register(Hospital)
admin.site.register(Owner)
admin.site.register(Feature)
admin.site.register(UserDetails)
admin.site.register(Booking)

