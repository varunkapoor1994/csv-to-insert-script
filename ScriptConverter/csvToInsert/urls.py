from . import views
from django.urls import path


app_name = 'csv-to-insert'
urlpatterns = [
    path('getheaders', views.getheaders, name='get_headers'),
    path('createscript', views.create_script, name='createScript'),
    path('', views.index, name='index')
]