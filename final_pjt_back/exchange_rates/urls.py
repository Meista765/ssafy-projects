from django.urls import path
from . import views

app_name = 'exchange_rates'
urlpatterns = [
    path("", views.get_and_response_exchange_rates, name='exchange'),
]