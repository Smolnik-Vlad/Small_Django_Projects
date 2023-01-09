from django.http import HttpResponse
from django.shortcuts import render
from first_proj.models import Category

def get_info_about_childhood(request):

    childhood_category = Category.objects.filter(title='childhood')
    if childhood_category:
        return HttpResponse(childhood_category[0].title)
    else:
        return HttpResponse('childhood is not available')


def get_info_about_youth(request):
    youth_category = Category.objects.filter(title='youth')
    if youth_category:
        return HttpResponse(youth_category[0].title)
    else:
        return HttpResponse('youth is not available')

def get_info_about_adulthood(request):
    adulthood_category = Category.objects.filter(title='youth')
    if adulthood_category:
        return HttpResponse(adulthood_category[0].title)
    else:
        return HttpResponse('youth is not available')
