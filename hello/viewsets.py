from rest_framework import viewsets
from .models import Game
from .serializers import GameSerializer


class GameViewSet(viewsets.ModelViewSet):
    # Define the query set that retrieves all records from the database
    queryset = Game.objects.all()
    # Define the translator serializer class to convert the objects
    serializer_class = GameSerializer