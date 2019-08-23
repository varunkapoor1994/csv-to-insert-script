from . import views
from django.urls import path

urlpatterns = [
    path('getheaders', views.getheaders, name='get_headers'),
    path('', views.index, name='index')
]