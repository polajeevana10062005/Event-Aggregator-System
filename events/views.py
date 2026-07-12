from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Event, Registration
from .forms import EventForm


def event_list(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'event_list.html', {'events': events})


@login_required
def create_event(request):
    form = EventForm(request.POST or None)

    if form.is_valid():
        event = form.save(commit=False)
        event.created_by = request.user
        event.save()
        return redirect('event_list')

    return render(request, 'event_create.html', {'form': form})


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'event_detail.html', {'event': event})


@login_required
def register_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    Registration.objects.create(user=request.user, event=event)
    return redirect('event_list')


def register(request):
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('event_list')

    return render(request, 'register.html', {'form': form})