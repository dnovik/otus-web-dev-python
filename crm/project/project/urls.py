
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('accounts.urls')),
    path('', include('contacts.urls')),
    path('', include('activities.urls')),
    path('', include('opportunities.urls'))
]
