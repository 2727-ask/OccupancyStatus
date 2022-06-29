from django.urls import path
from .  import views

urlpatterns = [
    path("",views.home, name="home"),
    path("results/",views.results, name="results"),
    path("signup_as_hptl/",views.signup_as_hptl, name="signup_as_hptl"),
    path("bookbed/<int:id>",views.bookbed, name="bookbed"),
    path("dbookings/",views.dbookings, name="dbookings"),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("details/",views.hospitalDetails,name="hospitalDetails"),
    path("bookings/",views.bookings,name="bookings"),
    path("signup/",views.signup,name="signup"),
    path("login/",views.user_login,name="login"),
    path("logout/",views.user_logout,name="log_out"),
    path("hospital/<int:id>",views.hospital,name="hospital")
]