from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("school_form/", views.school_form, name="school_form"),
    path("school_data/", views.SchoolDataAPI.as_view(), name="school_data"),
]
