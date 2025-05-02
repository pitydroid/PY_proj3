# accounts/models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    # Relación uno a uno con el modelo User. Si se borra el User, se borra el Profile.
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # Campo para la imagen de avatar. Se guardará en MEDIA_ROOT/avatars/
    # default= especifica una imagen por defecto si el usuario no sube ninguna.
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png', null=True, blank=True)
    # Campo para una breve biografía o descripción.
    bio = models.TextField(null=True, blank=True)
    # website = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        # Representación útil en el admin y debug
        return f'Perfil de {self.user.username}'