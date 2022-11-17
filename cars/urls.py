from django.urls import path

from .views import TippersListAPIView

app_name = 'cars'

urlpatterns = [
    path('', TippersListAPIView.as_view(), name='tippers_list'),
]
