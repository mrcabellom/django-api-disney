"""
Definition of urls for DjangoApiDisney
"""

from datetime import datetime
from django.conf.urls import patterns, url, include
from app.forms import BootstrapAuthenticationForm
from app import views as app_views
from django.contrib import admin
from django.contrib.auth import views as auth_views
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app_views.home, name='home'),
    url(r'^contact$', app_views.contact, name='contact'),
    url(r'^about', app_views.about, name='about'),
    url(r'^api/', include('attractions.urls')),
    url(r'^swagger/', include('rest_framework_swagger.urls')),
    url(r'^login/$',
        auth_views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        auth_views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls))
]
    