from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls, name='admin'),
                  path("", include("mainsite.urls")),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#handler404 = "gamelibs.views.page_not_found_view"