from django.contrib import admin
from django.urls import path, include
from users.urls import urlpatterns as users_urlpatterns


urlpatterns = [
    path('supersecret/', admin.site.urls),
    path('', include('tasks.urls')),
]

urlpatterns += users_urlpatterns
