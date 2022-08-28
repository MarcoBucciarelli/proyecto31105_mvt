from django.http import HttpResponse

from django.template import Context, Template

def probandohtml(request):
    nom = "Marco"
    apell = "Bucciarelli"
    dicc = {"nombre": nom, "apellido": apell}
    miarchivo = open("C:/Users/Usuario/Desktop/PythonProyecto1/plantillas/template1.html")
    contenido = miarchivo.read()
    miarchivo.close()
    plantilla = Template(contenido)
    contexto = Context(dicc) 
    documento = plantilla.render(contexto)
    return HttpResponse(documento)