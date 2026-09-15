from django.http import HttpResponse

def vista_uno(request):
    return HttpResponse("<h1>App 2 - Vista 1: Servicios</h1><p>Esta es la primera vista de la App 2.</p>")

def vista_dos(request):
    return HttpResponse("<h1>App 2 - Vista 2: Contacto</h1><p>Esta es la segunda vista de la App 2.</p>")