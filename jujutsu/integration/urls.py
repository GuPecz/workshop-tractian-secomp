from . import views
from django.urls import path

app_name = 'integration'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('listagem/', views.listagem, name='listagem'),
    path('export_csv/', views.export_csv, name='export_csv'),
]