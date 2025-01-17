from django.shortcuts import render

from django.shortcuts import render, redirect ##redirect sirve para redireccionar paginas
from .forms import LoginForm
from django.core.mail import EmailMessage
from django.urls import reverse
#from  .models import Registrarse
import hashlib
from app_registrarse.models import Registrarse

# Create your views here.
def login(request):
    #print("Tipo de petición: {}".format(request.method))  #method nos indica el metodo con el que se ha hecho la peticion
    login_form = LoginForm() #Hacemos la instancia del formulario
    if request.method == 'POST': #verificamos se el formulario se ha enviado por POST
        login_form = LoginForm(data= request.POST) #request.POST contiene los campos que hemos rellenado en el formulario
        if login_form.is_valid():  #verifica que todos los campos esten rellenados correctamente
            email= request.POST.get('email')
            contraseña=request.POST.get('contraseña')
            contraseña_cifrada= hashlib.sha1(contraseña.encode()).hexdigest()

            obj=Registrarse.objects.get(email=email, contraseña=contraseña_cifrada)
            if not obj.activate():
                return redirect(reverse('login')+'?fail') #reverse('contact') es como si fuera un tag url"""

    return render(request, "app_core/login.html", {'form':login_form})
