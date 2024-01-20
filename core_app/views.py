from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator

from .models import Notebooks, Images


def notebooks_list(request):
    notebooks = Notebooks.objects.prefetch_related("images").all()
    paginator = Paginator(notebooks, 25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
        "title": "Ноутбуки"
    }

    return render(request, "core_app/notebooks_list.html", context=context)

def notebook_detail(request, pk):
    data = Notebooks.objects.prefetch_related("images").get(pk=pk)

    return render(request, "core_app/notebook_detail.html", {"notebook": data})

def test(request):
    img = Images.objects.get(pk=1)
    return render(request, "core_app/test.html", {"img": img})