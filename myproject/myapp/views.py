from rest_framework import generics
from .models import SimpleModel
from .serializers import SimpleModelSerializer


class SimpleModelListView(generics.ListCreateAPIView):
    queryset = SimpleModel.objects.all()
    serializer_class = SimpleModelSerializer


class SimpleModelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SimpleModel.objects.all()
    serializer_class = SimpleModelSerializer
