from rest_framework import viewsets
from .serializers import ClienteSerializer
from .models import Cliente


class ClienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows clients to be viewed or edited.
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
