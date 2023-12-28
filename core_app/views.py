from django.shortcuts import render, HttpResponse
from .models import Notebooks

def notebooks_list(request):
    notebooks = Notebooks.objects.all()
    context = {
        "notebooks": notebooks,
        "title": "Ноутбуки"
    }

    return render(request, "core_app/notebooks_list.html", context=context)

