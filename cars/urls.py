from django.urls import path

from .views import index

app_name = 'cars'

urlpatterns = [
    path('', index, name='html_home'),
]
