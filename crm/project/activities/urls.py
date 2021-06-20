from django.urls import path
from . import views

urlpatterns = [
    path('activities/', views.ActivityLIst.as_view(), name='activities')
]