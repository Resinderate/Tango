from django.conf.urls import url

from games import views

urlpatterns = [
    url(r'^$', views.GameView.as_view(), name='game'),
]