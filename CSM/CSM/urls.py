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


# Django Imports
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

# Django Rest Framework:
from rest_framework import routers
from django.conf.urls import include

# Imported General Views:
from pages.views import landing
from pages.views import about_us
from pages.views import report_issue

# Imported API FBVs:
from api.views import (get_spell_information, spell_book, specific_user_character, user_character_names)

# Imported API ViewSets:
from api.views import (SubraceViewSet, RaceViewSet, PrestigeViewSet, ClassViewSet, FeatureViewSet, BackgroundViewSet,
                       SkillViewSet, LanguageViewSet, DamageTypeViewSet, ConditionViewSet, AlignmentViewSet,
                       ItemViewSet, WeaponPropertyViewSet, WeaponViewSet, ArmorViewSet, ToolViewSet, MountViewSet)

# Imported Account Views:
# from accounts.views import user_login
from accounts.views import user_logout
from accounts.views import user_home
from accounts.views import register_user

# DRF Configuration
router = routers.DefaultRouter()
router.register(r'rules/subraces', SubraceViewSet)
router.register(r'rules/races', RaceViewSet)
router.register(r'rules/prestige_classes', PrestigeViewSet)
router.register(r'rules/classes', ClassViewSet)
router.register(r'rules/features', FeatureViewSet)
router.register(r'rules/backgrounds', BackgroundViewSet)
router.register(r'rules/skills', SkillViewSet)
router.register(r'rules/languages', LanguageViewSet)
router.register(r'rules/damage_types', DamageTypeViewSet)
router.register(r'rules/conditions', ConditionViewSet)
router.register(r'rules/alignments', AlignmentViewSet)
router.register(r'equipment/items', ItemViewSet)
router.register(r'equipment/weapons', WeaponViewSet)
router.register(r'equipment/weapon_properties', WeaponPropertyViewSet)
router.register(r'equipment/armor', ArmorViewSet)
router.register(r'equipment/tools', ToolViewSet)
router.register(r'equipment/mounts_and_vehicles', MountViewSet)


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
    url(r'^user/characters/names/$', user_character_names, name='user_char_names'),
    url(r'^user/characters/specific_one/$', specific_user_character, name='specific_user_char'),

    # Company Information
    url(r'^about_us/$', about_us, name='contact'),
    url(r'^report_issue/$', report_issue, name='report'),



    # DRF configuration
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
