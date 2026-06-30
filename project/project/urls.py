from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
]


#======================================================================
# LOCAL APPS
#======================================================================

urlpatterns += [
    path('auth/', include('apps.authentication.urls')),
    path('system_console/', include('apps.system_console.urls')),
]


if settings.DEBUG:
    
    
    #======================================================================
    # SPECTACULAR
    #======================================================================

    urlpatterns += [
    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]