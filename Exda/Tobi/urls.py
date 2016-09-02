from django.conf.urls import url

from . import views

app_name = "Tobi"
urlpatterns = [
    url(r'^(?P<id>[0-9]+)/$', views.Basic_view.as_view()),
]