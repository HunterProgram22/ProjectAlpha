from django.conf.urls import url
from .views import Main

urlpatterns = [
            url(r'^$', Main.as_view(), name='LandingMain'),
            ]