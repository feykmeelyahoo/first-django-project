from django.conf.urls import url
from level2_ex import views

urlpatterns=[
    url(r'^$', views.index, name="index_level2_ex"),
    url(r'^revUser/', views.index2, name="index_level2_ex"),
]
