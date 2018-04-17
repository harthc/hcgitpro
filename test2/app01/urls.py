
from django.conf.urls import include, url
from app01.views import Sb
from app01 import views

urlpatterns = [

    url(r'showbook', views.showbook),
    url(r"add", views.add),
    url(r'delete/(\d+)', views.delete),
    url(r'select', views.select),
    url(r"sb$", Sb.as_view()),
]

# SB