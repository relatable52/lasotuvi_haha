from django.urls import include, re_path, path
from .views import api, lasotuvi_django_index
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    re_path(r'^api', api),
    re_path(r'^$', lasotuvi_django_index),
]