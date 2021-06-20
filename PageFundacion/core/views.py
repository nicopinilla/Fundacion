from django.shortcuts import redirect, render
from .models import Usuario, Relacion
from .forms import UsuarioForm
from .forms import InicioForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login

def home(request):
    return render(request, "core/home.html")
  

def registro(request, action, id):
    data = {"mesg": "", "form": UsuarioForm, "action": action, "id": id}
 
    if action == 'ins':
        if request.method == "POST":
            form = UsuarioForm(request.POST, request.FILES)
            if form.is_valid:
                try:
                    form.save()
                    data["mesg"] = "¡El usuario fue creado correctamente!"
                except:
                    data["mesg"] = "¡No se puede crear dos usuarios con el mismo rut!"
    return render(request, "core/registro.html", data)
    
def iniciar_sesion(request,action,id):
      data = {"mesg": "", "form": InicioForm, "action": action, "id": id}
      if action == 'ins':
        if request.method == "POST":
            form = InicioForm(request.POST, request.FILES)
            if form.is_valid:
                try:
                    
                    rut = form.cleaned_data['rut']
                    password = form.cleaned_data['password']
                    user = authenticate(rut=rut, password=password)
                except:
                    data["mesg"] = "¡Datos Incorrectos!"

        return render(request, "core/iniciar_sesion.html", data)

def aportador (request):
    if request.user.is_authenticated:
        return render(request, "core/aportador.html")
    # En otro caso redireccionamos al login
    return redirect('core/registro.html')
