from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Procesa el formulario si es válido
            nombre = form.cleaned_data['name']
            email = form.cleaned_data['mail']
            mensaje = form.cleaned_data['content']
            #Creamos el correo
            mail = EmailMessage(
                "Portfolio: nuevo mensaje de contacto", #asunto
                "De {} {}\n\nEscribió:\n\n{}".format(nombre, email, mensaje), #mensaje
                "PortafolioAlvaroConti", #email de origen - dominio de web
                ["alvaroconti05@gmail.com"], #Email de destino
                reply_to=[email]
            )

            #Enviamos y redireccionamos
            try:
                mail.send()
                return redirect(reverse('contact')+"?ok")
            except:
                return redirect(reverse('contact')+"?fail")
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
