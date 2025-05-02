# accounts/signals.py
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# Se ejecuta DESPUÉS de que un objeto User se guarda.
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Crea o actualiza el perfil del usuario.
    'created' es True si el User acaba de ser creado.
    'instance' es el objeto User que se guardó.
    """
    if created:
        # Si el usuario fue creado, crea su perfil.
        Profile.objects.create(user=instance)
    else:

        # Usamos hasattr para evitar errores si el perfil no existe por alguna razón.
        if hasattr(instance, 'profile'):
            instance.profile.save()
        else:
        
            Profile.objects.create(user=instance)