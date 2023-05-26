from django.http import HttpResponse

def first(request):
    return HttpResponse("<h1>Hello World</h1>")


def second_func(request):
    return HttpResponse("Акын")

def third(request):
    return HttpResponse("<h1>УРАААААААААААААААААА</h1>")