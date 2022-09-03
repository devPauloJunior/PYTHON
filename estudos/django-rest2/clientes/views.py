from rest_framework import viewsets
from clientes.serializers import ClienteSerializer
from clientes.models import Cliente

class ClientesViewSet(viewsets.ModelViewSet):
    """ Listando todos os clientes """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    