from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def cookie(request):
    print(request.COOKIES)


def session(request):
    num_of_vis = request.session.get('num_of_vis', 0) + 1
    request.session['num_of_vis'] = num_of_vis
    if num_of_vis > 4:
        del request.session['num_of_vis']

    return HttpResponse('view count='+str(num_of_vis))
