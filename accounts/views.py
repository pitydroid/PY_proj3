# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Profile

def signup_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Guarda el nuevo usuario
            # Opcional: Loguear al usuario inmediatamente después del registro
            login(request, user)
            messages.success(request, f'¡Registro exitoso! Bienvenido/a {user.username}.')
            # Redirige a la página principal
            return redirect('site_home')
        else:
            # Si hay errores, se mostrarán en la plantilla
            messages.error(request, 'Hubo errores en el formulario. Por favor revisa los campos.')
    else: # Si es GET, muestra el formulario vacío
        form = UserRegisterForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def profile_edit_view(request):
    # Usamos get_or_create por si el perfil no existía por alguna razón
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        # Pasamos request.POST para datos normales y request.FILES para archivos
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, '¡Tu perfil se ha actualizado correctamente!')
            return redirect('profile_view') # Vuelve a la vista de perfil
        else:
            # Si hay errores, se quedan en la misma página y los formularios los mostrarán
             messages.error(request, 'Por favor corrige los errores marcados abajo.')
    else: # Si es una petición GET, muestra los formularios con datos actuales
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'accounts/profile_edit.html', context)

@login_required
def profile_view(request):
    # Usamos try/except o get_or_create para manejar si el perfil no existe
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        # Si no existe
        profile = Profile.objects.create(user=request.user)

    context = {
        'user': request.user,
        'profile': profile
    }
    return render(request, 'accounts/profile.html', context)