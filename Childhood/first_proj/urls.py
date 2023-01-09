from django.urls import path

from first_proj.views import get_info_about_childhood, get_info_about_youth, get_info_about_adulthood

urlpatterns = [
    path('childhood/', get_info_about_childhood),
    path('youth/', get_info_about_youth),
    path ('adulthood/', get_info_about_adulthood)

]
