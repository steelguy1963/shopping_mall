"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from product import views as product_view
from users import views as users_view
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView
from . import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', users_view.signup),
    url(r'^accounts/register/profile/$', users_view.editProfile),
    url(r'^list/$', product_view.listProduct),
    url(r'^list/(?P<product_id>\d+)/$', product_view.showProduct),
    url(r'^product/delete/(?P<product_id>\d+)/$',product_view.deleteProduct),
    url(r'^list_edit/$', product_view.listProduct_edit),
    url(r'^list_edit/create/$', product_view.createProduct),
    url(r'^list_edit/(?P<product_id>\d+)/$', product_view.editProduct),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
