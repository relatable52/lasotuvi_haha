from django.urls import include, re_path
from .views import api, lasotuvi_django_index

urlpatterns = [
    re_path(r'^api', api),
    re_path(r'^$', lasotuvi_django_index)
]