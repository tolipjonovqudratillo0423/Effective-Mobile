from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
]


#======================================================================
# LOCAL APPS
#======================================================================

urlpatterns += [
    path('auth/', include('apps.authentication.urls')),
]
