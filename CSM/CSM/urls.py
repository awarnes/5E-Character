"""CSM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

# Django Rest Framework
from rest_framework import routers
from django.conf.urls import include

# Imported General Views
from pages.views import landing
from pages.views import about_us
from pages.views import report_issue

# Imported API Views
from api.views import get_spell_information
from api.views import spell_book

# Imported Account View
# from accounts.views import user_login
from accounts.views import user_logout
from accounts.views import user_home
from accounts.views import register_user

# DRF Configuration
# router = routers.DefaultRouter()
# router.register(r'spells/spell_info', SpellViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Home Page
    url(r'^$', landing, name='landing'),

    # Spells Interface
    url(r'^spells/$', spell_book, name='spells'),
    url(r'^spells/spell/$', get_spell_information, name='spell_info'),

    # User Accounts
    url(r'^login/$', auth_views.login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^register/$', register_user, name='register'),
    url(r'^logout/$', user_logout, name='logout'),

    # User Profile
    url(r'^home/$', user_home, name='home'),

    # Company Information
    url(r'^about_us/$', about_us, name='contact'),
    url(r'^report_issue/$', report_issue, name='report'),



    # DRF configuration
    # url(r'^api/v1/', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
