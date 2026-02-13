from django.db import models

from django.db import models
from tickets.models import Ticket

class CheckIn(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    checkin_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Check-in {self.ticket.participant_name}"
