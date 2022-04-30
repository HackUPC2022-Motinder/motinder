from apps.recommender.models import Motorcycle
from rest_framework import viewsets
from rest_framework import permissions
from apps.recommender.serializer import MotorcycleSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Motorcycle.objects.all()
    serializer_class = MotorcycleSerializer
    permission_classes = [permissions.IsAuthenticated]