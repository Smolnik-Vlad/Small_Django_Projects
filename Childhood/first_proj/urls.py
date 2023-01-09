from django.urls import path

from first_proj.views import life_period, get_info_about_choosen_period

urlpatterns = [
    path('<str:period>/', get_info_about_choosen_period),


]
