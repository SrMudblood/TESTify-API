from django.urls import path
from .infrastructure.drivers.for_get_data_API_adapter import For_get_data_API_adapter as API_adapter

urlpatterns = [
    path('person/v1/', API_adapter().get_normal_person),
]