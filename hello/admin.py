# your_app/admin.py
from django.contrib import admin
from .models import Game  # Import your model

# Register your model here
admin.site.register(Game)