from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def homePage(self):
    return HttpResponse("Hello World")


def about(request, author_no=0):
    html = "<h2>Here is Author:{}'s aboutpage!</h2><hr>".format(author_no)
    return HttpResponse(html)


def company(request):
    return HttpResponse("mycompany")


def sales(request):
    return HttpResponse("mysales")


def contact(request):
    return HttpResponse("contact")