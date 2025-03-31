from __future__ import absolute_import, unicode_literals, division

from django.urls import re_path

from .api import LockAPIView

__all__ = ('urlpatterns', )

urlpatterns = [
    re_path(r'api/lock/(?P<app>[\w-]+)/(?P<model>[\w-]+)/$',
        LockAPIView.as_view(), name='locking-api'),

    re_path(r'api/lock/(?P<app>[\w-]+)/(?P<model>[\w-]+)/(?P<object_id>\d+)/$',
        LockAPIView.as_view(), name='locking-api'),
]
