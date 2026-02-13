from django.db import models

import uuid
from django.db import models
from events.models import Event

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participant_name = models.CharField(max_length=200)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=20)
    qr_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.participant_name} - {self.event.name}"
