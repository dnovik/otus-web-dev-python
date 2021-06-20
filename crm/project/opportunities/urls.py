from django.urls import path
from . import views

urlpatterns = [
    path('opportunities/', views.OpportunityLIst.as_view(), name='opportunities'),
    path('opportunities/add/', views.OpportunityCreate.as_view(), name='opportunity_add'),
    path('opportunities/<int:opportunity_pk>', views.OpportunityDetail.as_view(), name='opportunity')
]

