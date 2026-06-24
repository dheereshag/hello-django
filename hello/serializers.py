from rest_framework import serializers
from .models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        # '__all__' is a shortcut to include all model columns (id, title, publisher, price) in JSON
        fields = '__all__'