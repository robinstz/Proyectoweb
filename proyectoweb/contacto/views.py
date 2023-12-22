from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage
# Create your views here.

def contactanos(request):
    formulario_contacto=FormularioContacto()

    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            email=EmailMessage("Mensaje DE Django",
            "El usuario {} con la dirección {} comento lo siguiente:\n\n {}".format(nombre,email,contenido),
            "",["danilitosatz@gmail.com"],reply_to=[email])

            try:
                email.send() 
                return redirect("/Contactanos/?valido")
            
            except:
                return redirect("/Contactanos/?novalido")

    return render(request, 'contacto/contact.html', {'miFormulario':formulario_contacto})