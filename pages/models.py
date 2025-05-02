from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Page(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=255, blank=True, null=True) # NUEVO CAMPO
    content = RichTextField() # CAMBIADO a RichTextField
    image = models.ImageField(upload_to='pages/', null=True, blank=True) # NUEVO CAMPO (upload_to crea subcarpeta en media/)
    publication_date = models.DateTimeField(auto_now_add=True) # O mantén default=timezone.now si prefieres
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pages') # CAMBIADO a User

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publication_date'] # Ordenar por fecha