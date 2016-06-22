"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework import routers
from server.main import views

router = routers.DefaultRouter()
router.register(r'shortener', views.Shortener_ViewSet)

urlpatterns = [
    url(r'^(?P<type>css)/(?P<path>.+\.css)$', views.File),
    url(r'^(?P<type>js)/(?P<path>.+\.js)$', views.File),
    url(r'^api/v1/', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^(?P<token>[a-zA-Z0-9]+)$', views.Redirect),
    url(r'^$', views.Index),
]

handler404 = views.handler404

