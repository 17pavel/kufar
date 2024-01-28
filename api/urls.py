from django.urls import path, include
from core_app.models import Notebooks, Images
from rest_framework import routers, serializers, viewsets, permissions, filters


# Serializers define the API representation.
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = "id", "image", "notebook"


class NotebookSerializer(serializers.HyperlinkedModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = Notebooks
        fields = "__all__"
# ViewSets define the view behavior.


class NotebookViewSet(viewsets.ModelViewSet):
    queryset = Notebooks.objects.prefetch_related("images").all()
    serializer_class = NotebookSerializer
    permission_classes = [permissions.IsAdminUser]
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ("title", "description")


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
