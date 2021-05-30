
from django.contrib import admin
from django.urls import path, include
from django101.cities.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('cities/', include('django101.cities.urls')),
    path('', include('django101.people.urls')),
]
