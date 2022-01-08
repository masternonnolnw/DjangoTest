from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Room, Topic
from .form import Roomform

# Create your views here.

# rooms = [
#     {'id': 1, 'name': "master"},
#     {'id': 2, 'name': "master2"},
#     {'id': 3, 'name': "master3"},
# ]


def home(req):
    q = ''
    if req.GET.get('q') != None:
        q = req.GET.get('q')
    rooms = Room.objects.filter(topic__name__icontains=q)

    topic = Topic.objects.all()

    context = {'rooms': rooms, "topics": topic}
    return render(req, 'base/home.html', context)


def room(req, pk):
    # room = None
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(req, 'base/room.html', context)


def createRoom(req):
    form = Roomform()
    if req.method == 'POST':
        form = Roomform(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(req, 'base/room_form.html', context)


def updateRoom(req, pk):
    room = Room.objects.get(id=pk)
    form = Roomform(instance=room)

    if req.method == 'POST':
        form = Roomform(req.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(req, 'base/room_form.html', context)


def deleteRoom(req, pk):
    room = Room.objects.get(id=pk)
    if req.method == 'POST':
        room.delete()
        return redirect('home')

    return render(req, 'base/delete.html', {'obj': room})
