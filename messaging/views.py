# messaging/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Message
from .forms import MessageForm # Importa el formulario
from django.contrib import messages

@login_required
def inbox_view(request):
    # Obtener usuarios únicos con los que se ha intercambiado mensajes
    # (Excluyendo al propio usuario)
    user_ids = Message.objects.filter(
        Q(sender=request.user) | Q(receiver=request.user)
    ).values_list('sender_id', 'receiver_id')

    # Aplanar la lista de IDs y eliminar duplicados y el propio ID
    related_user_ids = set(uid for pair in user_ids for uid in pair if uid != request.user.id)

    users_list = User.objects.filter(id__in=related_user_ids).order_by('username')

    # Opcional: Podrías añadir lógica para contar mensajes no leídos por conversación

    context = {
        'users_list': users_list
    }
    return render(request, 'messaging/inbox.html', context)

@login_required
def conversation_detail_view(request, username):
    # Obtener el otro usuario o error 404
    other_user = get_object_or_404(User, username=username)

    # No permitir conversar consigo mismo
    if other_user == request.user:
        messages.error(request, "No puedes enviarte mensajes a ti mismo.")
        return redirect('inbox')

    # Obtener mensajes entre ambos usuarios
    conversation_messages = Message.objects.filter(
        (Q(sender=request.user) & Q(receiver=other_user)) |
        (Q(sender=other_user) & Q(receiver=request.user))
    ).order_by('timestamp') # Ordenar por fecha

    # Marcar mensajes recibidos como leídos al ver la conversación
    Message.objects.filter(sender=other_user, receiver=request.user, is_read=False).update(is_read=True)

    # Manejar envío de nuevo mensaje
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            Message.objects.create(
                sender=request.user,
                receiver=other_user,
                content=form.cleaned_data['content']
            )
            # Redirigir a la misma página para ver el mensaje enviado
            return redirect('conversation_detail', username=other_user.username)
    else: # Si es GET, mostrar formulario vacío
        form = MessageForm()

    context = {
        'other_user': other_user,
        'messages': conversation_messages,
        'form': form,
    }
    return render(request, 'messaging/conversation_detail.html', context)

# Vista para listar todos los usuarios (para iniciar nuevas conversaciones)
@login_required
def user_list_view(request):
     users = User.objects.exclude(pk=request.user.pk).order_by('username')
     context = {
          'all_users': users
     }
     return render(request, 'messaging/user_list.html', context)