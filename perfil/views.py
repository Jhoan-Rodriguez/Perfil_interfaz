from django.shortcuts import render, redirect
from .forms import PerfilForm
from .models import Perfil

def perfil_view(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = PerfilForm()

    # Puedes obtener los perfiles guardados y enviarlos al template
    perfiles = Perfil.objects.all()
    return render(request, 'perfil/perfil.html', {'form': form, 'perfiles': perfiles})