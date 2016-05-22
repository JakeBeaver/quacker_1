"""poster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers
from app import views

from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()

router.register(r'apifetch/id=(?P<post_id>[0-9]{0,30})', views.fetch_id, 'api-fetch-id')
router.register(r'apifetch/(?P<name>[a-zA-Z0-9.+\-_@]{0,30})', views.fetch, 'api-fetch-filter')
router.register(r'apifetch', views.authpost, 'api-fetch')
router.register(r'authpost', views.authpost, 'authpost')


router.register(r'comments/(?P<identification>[0-9]{0,30})', views.fetch_com, 'comment-filter')
router.register(r'comments', views.comment, 'comment')


router.register(r'user', views.UserViewSet, 'user')

urlpatterns = [

	url(r'^', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^accounts/', include('accounts.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^aut/', 'app.views.authpost'),
    url(r'^fetch/(?P<name>[a-zA-Z0-9.+-_@]{0,30})//?$', 'app.views.fetch', name='fetch'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
