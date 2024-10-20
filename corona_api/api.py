from .models import Corona
from rest_framework import viewsets, permissions
from .serializers import CoronaSerializer

class CoronaViewSet(viewsets.ModelViewSet):
    queryset = Corona.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CoronaSerializer