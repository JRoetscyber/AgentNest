from django.urls import path
from .views import home_page

app_name = 'apps.leads'  # Namespace for the leads app

urlpatterns = [
    path('', home_page, name='home')
]