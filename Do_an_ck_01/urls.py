"""Do_an_ck_01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.conf import settings

# API
from rest_framework import routers
from Do_an_01.views import StorytViewSet
router = routers.DefaultRouter()
router.register('story', StorytViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Do_an_01.urls')),
    path('', include('customers_hdg.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),

]
# Static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# Media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)