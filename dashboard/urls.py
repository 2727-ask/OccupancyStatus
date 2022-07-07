from django.urls import path
from . import views

urlpatterns = [
    path('', views.Dashboard.as_view(), name="dashboard"),
    path('edit-profile/', views.EditProfile.as_view(), name="dashboard"),
    path('facilites/', views.FacilitiesView.as_view(), name="dashboard"),
    path('facilites/<int:id>', views.FacilitiesUpdateView.as_view(), name="dashboard"),
    path('doctors/', views.DoctorsView.as_view(), name="dashboard"),
    path('doctors/<int:id>', views.DoctorsUpdateView.as_view(), name="dashboard"),
    path('owners/', views.OwnersView.as_view(), name="dashboard"),
    path('owners/<int:id>', views.OwnerUpdateView.as_view(), name="dashboard"),
    path('images/', views.UploadImageView.as_view(), name="dashboard"),
    path('manage-bookings/', views.ManageBookings.as_view(), name="dashboard"),
]
