from django.urls import path
from .views import notebooks_list, notebook_detail, test

urlpatterns = [
    path("test/", test),
    path('', notebooks_list, name="notebooks"),
    path("<int:pk>", notebook_detail, name="notebook_detail"),

]
