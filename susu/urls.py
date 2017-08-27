from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from susu import views

urlpatterns = [
    url(r'^clients/$', views.ClientList.as_view()),
    url(r'^clients/(?P<pk>[0-9]+)/$', views.ClientDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
