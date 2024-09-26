from django.urls import path
from infoimages.views import save_data
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('api/save-data/', save_data, name='save_data'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)