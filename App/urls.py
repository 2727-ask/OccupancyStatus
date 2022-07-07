from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signing_as/", views.SignInAs.as_view(), name="signingAs"),
    path("signing_as/user", views.SignInAsUser.as_view(), name="signingAs"),
    path("signing_as/hospital", views.SignUpAsHospital.as_view(), name="signingAs"),
    path("user-info/", views.UserInformationView.as_view(), name="user-info"),
    path("hospital-info/", views.HospitalInformationView.as_view(), name="hospital-info"),
    path("hospital-social-info/", views.HospitalSocialInformationView.as_view(), name="hospital-info"),
    path("results/", views.results, name="results"),
    path("signup_as_hptl/", views.signup_as_hptl, name="signup_as_hptl"),
    path("bookbed/<int:id>", views.bookbed, name="bookbed"),
    path("dbookings/", views.dbookings, name="dbookings"),
    path("details/", views.hospitalDetails, name="hospitalDetails"),
    path("bookings/", views.bookings, name="bookings"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="log_out"),
    path("hospital/<int:id>", views.hospital, name="hospital")
]
