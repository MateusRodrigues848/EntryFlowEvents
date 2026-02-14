from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


import uuid
import qrcode
from io import BytesIO
from django.core.files import File
from django.db import models

class Participant(models.Model):
    PARTICIPANT_TYPES = [
        ('visitante', 'Visitante'),
        ('expositor', 'Expositor'),
        ('produtor', 'Produtor Rural'),
    ]

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='participants')
    name = models.CharField(max_length=200)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=20)
    participant_type = models.CharField(max_length=20, choices=PARTICIPANT_TYPES)
    qr_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    qr_image = models.ImageField(upload_to='qrcodes/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.qr_image:
            qr = qrcode.make(str(self.qr_code))
            buffer = BytesIO()
            qr.save(buffer, format='PNG')
            filename = f'{self.qr_code}.png'
            self.qr_image.save(filename, File(buffer), save=False)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.event.name}"
