from django.shortcuts import render

def index(request):
    return render(request, "shows/index.html")


def stage(request, room_name):
    return render(request, "shows/stage.html", {"room_name": room_name})