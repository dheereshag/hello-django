from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import GameViewSet

# Initialize the router
router = DefaultRouter()
# Register the viewsets: the first argument is the prefix, the second is the ViewSet class
# Registered prefix 'games' creates routes like /api/games/ and /api/games/{id}/
router.register(r'games', GameViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include all router urls under /api/
    path('api/', include(router.urls)),
]