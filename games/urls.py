from django.conf.urls import url

from games import views

urlpatterns = [
    url(r'^$', views.game, name='game'),
]