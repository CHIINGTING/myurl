import math

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse


# Create your views here.


def homePage(self):
    year = 2019
    month = 10
    day = 21
    postid = 3
    html = "<a href='{}'>show the post link</a>".format(reverse('post-url', args=(year, month, day, postid)))
    return HttpResponse(html)


def about(request, author_no=0):
    html = "<h2>Here is Author:{}'s aboutpage!</h2><hr>".format(author_no)
    return HttpResponse(html)


def company(request):
    return HttpResponse("mycompany")


def sales(request):
    return HttpResponse("mysales")


def contact(request):
    return HttpResponse("contact")


def listing(request, yr, mon, day):
    return HttpResponse("Your Date List is {}/{}/{}".format(yr, mon, day))


def post(request, yr, mon, day, post_num):
    html = "Today is {}/{}/{}, the post is {}".format(yr, mon, day, post_num)
    return HttpResponse(html)


def post2(request, yr, mon, day, post_num):
    year = yr
    month = mon
    days = day
    postNum = post_num
    return render(request, 'post2.html', locals())


def mul(request, x, y):
    sumX = x
    sumY = y
    sumMul = sumX * sumY
    return render(request, 'mul.html', locals())


def temC(request, tem):
    temc = tem
    temf = math.ceil((tem-32)*5/9)
    return render(request, 'temC.html', locals())


def temF(request, tem):
    temf = tem
    temc = math.ceil(tem*5/9 + 32)
    return render(request, 'temF.html', locals())