
from django.contrib import admin
import debug_toolbar
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('', include('main.urls')),
    path('', include('activities.urls')),
    path('', include('opportunities.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('accounts.urls')),
    path('api/', include('contacts.urls'))
]
