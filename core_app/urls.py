from django.urls import path
from .views import notebooks_list


urlpatterns = [

    path('', notebooks_list)
]
