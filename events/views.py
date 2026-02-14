from django.shortcuts import render, redirect
from .forms import EventForm, Event
from django.contrib.auth.decorators import login_required

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
