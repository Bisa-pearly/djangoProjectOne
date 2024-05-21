from django.http import HttpResponse


def sayHello(request):
    return HttpResponse('Hello World bikash!')

def sayHello2(request,name):
    return HttpResponse("I am second call , %s" %name)