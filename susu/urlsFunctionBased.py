from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from susu import viewsFunctionBased

urlpatterns = [
    url(r'^clients/$', viewsFunctionBased.client_list),
    url(r'^clients/(?P<pk>[0-9]+)/$', viewsFunctionBased.client_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)