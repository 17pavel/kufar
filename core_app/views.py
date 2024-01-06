from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator

from .models import Notebooks


def notebooks_list(request):
    notebooks = Notebooks.objects.all()
    paginator = Paginator(notebooks, 25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
        "title": "Ноутбуки"
    }

    return render(request, "core_app/notebooks_list.html", context=context)

def notebook_detail(request, pk):
    data = Notebooks.objects.get(pk=pk)

    return render(request, "core_app/notebook_detail.html", {"notebook": data})