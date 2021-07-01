from django.urls import path
from . import views

urlpatterns = [
    path('activities/', views.ActivityLIst.as_view(), name='activities'),
    path('activities/<int:activity_pk>', views.ActivityDetail.as_view(), name='activity'),
    path('activities/add/', views.ActivityCreate.as_view(), name='activity_add'),
    path('activities/<int:activity_pk>/edit', views.ActivityUpdate.as_view(), name='activity_edit'),
    path('activities/<int:activity_pk>/delete', views.ActivityDelete.as_view(), name='activity_delete')
]
