from django.shortcuts import render
from django.http import JsonResponse


def analysis(req):
    return JsonResponse({
        'info': 'Django Server'
    })
