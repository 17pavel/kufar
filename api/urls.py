from dataclasses import field

from django.urls import path, include
from core_app.models import Notebooks, Images
from rest_framework import routers, serializers, viewsets, permissions


# Serializers define the API representation.
class NotebookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notebooks
        fields = "__all__"
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = "id", "image", "notebook"

# ViewSets define the view behavior.
class NotebookViewSet(viewsets.ModelViewSet):
    queryset = Notebooks.objects.prefetch_related("images").all()
    serializer_class = NotebookSerializer
    permission_classes = [permissions.IsAdminUser]

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.select_related("notebook").all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAdminUser]

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'notebook', NotebookViewSet)
router.register(r'image', ImageViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]