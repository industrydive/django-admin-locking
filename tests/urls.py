from __future__ import absolute_import, unicode_literals, division

from django.conf import settings
from django.conf.urls import include
from django.contrib import admin
from django.urls import re_path

__all__ = ('urlpatterns', )

admin.autodiscover()
urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^admin/locking/', include('locking.urls'))
]
if settings.GRAPPELLI_INSTALLED:
    urlpatterns = [re_path(r'^grappelli/', include('grappelli.urls'))] + urlpatterns
