from django.shortcuts import render, redirect, get_object_or_404
from .forms import EventForm, Event
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Participant, CheckIn
from django.db.models import Count

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user  # 🔥 AQUI está o pulo do gato
            event.save()
            return redirect('event_list')
    else:
        form = EventForm()

    return render(request, 'events/create_event.html', {'form': form})

@login_required
def event_list(request):
    events = Event.objects.filter(organizer=request.user)
    return render(request, 'events/event_list.html', {'events': events})


@login_required
def checkin_view(request, qr_code):
    participant = get_object_or_404(Participant, qr_code=qr_code)

    today = timezone.now().date()

    already_checked = CheckIn.objects.filter(
        participant=participant,
        checkin_time__date=today
    ).exists()

    if already_checked:
        message = " ⚠️ Participante ja realizou o chek-in hoje."
    else:
        CheckIn.objects.create(participant=participant)
        message = "✅ Ckeck-in realizado com sucesso!"

    return render(request, 'events/checkin_result.html', {
        'participant': participant,
        'message': message
    })



@login_required
def event_dashboard(request, event_id):
    event = get_object_or_404(Event, id=event_id, organizer=request.user)

    total_participants = event.participants.count()

    today = timezone.now().date()

    checkins_today = CheckIn.objects.filter(
        participant__event=event,
        checkin_time__date=today
    ).count()

    total_checkins = CheckIn.objects.filter(
        participant__event=event
    ).count()

    presence_percentage = 0
    if total_participants > 0:
        presence_percentage = (checkins_today / total_participants) * 100

    participants = event.participants.all()

    context = {
        'event': event,
        'total_participants': total_participants,
        'checkins_today': checkins_today,
        'total_checkins': total_checkins,
        'presence_percentage': round(presence_percentage, 2),
        'participants': participants,
    }

    return render(request, 'events/dashboard.html', context)

def portaria_checkin(request, qr_code):
    participant = get_object_or_404(Participant, qr_code=qr_code)

    today = timezone.now().date()

    already_checked = CheckIn.objects.filter(
        participant=participant,
        checkin_time__date=today
    ).exists()

    if already_checked:
        status = "duplicado"
    else:
        CheckIn.objects.create(participant=participant)
        status = "sucesso"

    return render(request, 'events/portaria.html', {
        'participant': participant,
        'status': status,
        'now': timezone.now()
    })
