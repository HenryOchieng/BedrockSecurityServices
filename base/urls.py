from django.urls import path
from .views import ServiceListAndFormView

urlpatterns = [
    path('', ServiceListAndFormView.as_view(), name='base'),
]