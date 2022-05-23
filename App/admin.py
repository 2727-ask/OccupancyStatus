from django.contrib import admin
from .models import Doctors,Hospital,Owner,Feature
# Register your models here.
admin.site.register(Doctors)
admin.site.register(Hospital)
admin.site.register(Owner)
admin.site.register(Feature)

