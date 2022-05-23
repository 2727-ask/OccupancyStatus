from django.urls import path
from .  import views

urlpatterns = [
    path("",views.home, name="home"),
    path("results/",views.results, name="results"),
    path("hospital/<int:id>",views.hospital,name="hospital")
]