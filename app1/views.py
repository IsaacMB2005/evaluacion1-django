from django.http import HttpResponse

def vista_uno(request):
    return HttpResponse("<h1>App 1 - Vista 1: Inicio</h1><p>Esta es la primera vista de la App 1.</p>")

def vista_dos(request):
    return HttpResponse("<h1>App 1 - Vista 2: Acerca de</h1><p>Esta es la segunda vista de la App 1.</p>")