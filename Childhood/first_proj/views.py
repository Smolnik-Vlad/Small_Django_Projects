from django.http import HttpResponse
from django.shortcuts import render

from first_proj.func.get_info import life_period
from first_proj.models import Category

def get_info_about_choosen_period(request, period: str):


    result: str = life_period(check_period=period)
    if result:
        return HttpResponse(result, content_type='text/plain; charset=utf-8')
    else:
        return HttpResponse(f'{period} is not available')
    #return HttpResponse(f"SO: {result}")

