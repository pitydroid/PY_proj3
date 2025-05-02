# messaging/models.py
from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages', verbose_name="Remitente")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages', verbose_name="Destinatario")
    content = models.TextField(verbose_name="Contenido")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Envío")
    is_read = models.BooleanField(default=False, verbose_name="Leído")

    def __str__(self):
        return f"De {self.sender.username} para {self.receiver.username} ({self.timestamp.strftime('%d-%m-%Y %H:%M')})"

    class Meta:
        ordering = ['timestamp'] # Ordenar mensajes por fecha
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"