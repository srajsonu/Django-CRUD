from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def cookie(request):
    print(request.COOKIES)
    oldVal = request.COOKIES.get('zap', None)
    resp = HttpResponse('In a view - the zap cookie value is ' + str(oldVal))
    if oldVal:
        resp.set_cookie('zap', int(oldVal) + 1)  # No expired date = until browser close
    else:
        resp.set_cookie('zap', 42)  # No expired date = until browser close

    resp.set_cookie('sakaicar', 42, max_age=1000)  # seconds until expire
    return resp


def session(request):
    num_of_vis = request.session.get('num_of_vis', 0) + 1
    request.session['num_of_vis'] = num_of_vis
    if num_of_vis > 4:
        del request.session['num_of_vis']

    return HttpResponse('view count='+str(num_of_vis))

def owner(request):
    return HttpResponse("Hello, world. d465f14a is the polls index.")
