from django.urls import path
from . import views

urlpatterns = [
    path('', views.OpportunityLIst.as_view(), name='opportunities'),
    path('add/', views.OpportunityCreate.as_view(), name='opportunity_add')
]

