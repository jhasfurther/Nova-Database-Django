from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def media(request):
    return HttpResponse("Hello, media file!")

