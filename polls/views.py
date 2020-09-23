from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. cc5f52c9 is the polls index.")