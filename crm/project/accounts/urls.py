from django.urls import path
from . import views

urlpatterns = [
    path('accounts/', views.AccountItemListView.as_view()),
    path('accounts/<int:pk>/', views.AccountItemDetailView.as_view())
]
