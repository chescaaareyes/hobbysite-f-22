from django.http import HttpResponse
from django.shortcuts import render


def forum_list(request):
    return HttpResponse("Hello Forum List!")


def forum_detail(request):
    return HttpResponse("Hello Forum Detail!")
