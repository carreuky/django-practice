from django.http import HttpResponse


def index(request): 
    return HttpResponse("Hello, world. This is the index view of Demoapp.")

def salamu(request):
    return HttpResponse('salamu za sasa')