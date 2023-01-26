from django.http import HttpResponse


def index(request): 
    return HttpResponse("Hello, world. This is the index view of Demoapp.")

def salamu(request):
    return HttpResponse('salamu za sasa')

def pathview(request, name, id): 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 
def handler404(request, exception):
    return HttpResponse('404 erorr')