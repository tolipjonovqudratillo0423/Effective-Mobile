from django.urls import path

from apps.system_console.views import (
    BEListCreateAPIView,
    BERetrieveUpdateDelete,
    ARListCreateAPIView,
    ARRetrieveUpdateDelete
)

urlpatterns = [
    path("business_elements/", BEListCreateAPIView.as_view(), name="be_lc"),
    path("business_elements/<int:pk>/", BERetrieveUpdateDelete.as_view(), name="be_rud"),
    
    path("access_rules/", ARListCreateAPIView.as_view(), name="ar_lc"),
    path("access_rules/<int:pk>/", ARRetrieveUpdateDelete.as_view(), name="ar_rud"),
]
