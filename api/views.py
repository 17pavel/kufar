from django.shortcuts import render
from rest_framework import routers, serializers, viewsets, permissions, filters
from django_filters import OrderingFilter
from api.urls import ImageSerializer, NotebookSerializer
from core_app.models import Notebooks, Images



# Create your views here.
