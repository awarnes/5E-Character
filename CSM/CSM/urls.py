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
from pages.views import about_us, report_issue
from pages.views import search_home
from pages.views import (spell_details, subrace_details, race_details, prestige_details, class_details, feature_details,
                         background_details, skill_details, language_details, condition_details, item_details, weapon_details,
                         armor_details, tool_details, mount_details)

# Imported API FBVs:
from api.views import (spell_book, specific_user_character, user_character_names)

# Imported API ViewSets:
from api.views import (SubraceViewSet, RaceViewSet, PrestigeViewSet, ClassViewSet, FeatureViewSet, BackgroundViewSet,
                       SkillViewSet, LanguageViewSet, DamageTypeViewSet, ConditionViewSet, AlignmentViewSet, SpellViewSet,
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
router.register(r'equipment/armors', ArmorViewSet)
router.register(r'equipment/tools', ToolViewSet)
router.register(r'equipment/mounts_and_vehicles', MountViewSet)
router.register(r'spells/spell', SpellViewSet)



urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Home Page
    url(r'^$', landing, name='landing'),

    # Spells Interface
    url(r'^spells/$', spell_book, name='spells'),

    # User Accounts
    url(r'^login/$', auth_views.login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^register/$', register_user, name='register'),
    url(r'^logout/$', user_logout, name='logout'),

    # User Profile
    url(r'^home/$', user_home, name='home'),
    url(r'^user/characters/names/$', user_character_names, name='user_char_names'),
    url(r'^user/characters/specific_one/$', specific_user_character, name='specific_user_char'),

    # Database Detail Pages:
    url(r'^spells/details/(?P<slug>(\w+[a-z\-]+))', spell_details, name='spell_details'),
    url(r'^subraces/details/(?P<slug>(\w+[a-z\-]+))', subrace_details, name='subrace_details'),
    url(r'^races/details/(?P<slug>(\w+[a-z\-]+))', race_details, name='race_details'),
    url(r'^prestige_classes/details/(?P<slug>(\w+[a-z\-]+))', prestige_details, name='prestige_details'),
    url(r'^classes/details/(?P<slug>(\w+[a-z\-]+))', class_details, name='class_details'),
    url(r'^features/details/(?P<slug>(\w+[a-z\-]+))', feature_details, name='feature_details'),
    url(r'^backgrounds/details/(?P<slug>(\w+[a-z\-]+))', background_details, name='background_details'),
    url(r'^skills/details/(?P<slug>(\w+[a-z\-]+))', skill_details, name='skill_details'),
    url(r'^languages/details/(?P<slug>(\w+[a-z\-]+))', language_details, name='language_details'),
    url(r'^conditions/details/(?P<slug>(\w+[a-z\-]+))', condition_details, name='condition_details'),
    url(r'^items/details/(?P<slug>(\w+[a-z\-]+))', item_details, name='item_details'),
    url(r'^weapons/details/(?P<slug>(\w+[a-z\-]+))', weapon_details, name='weapon_details'),
    url(r'^armors/details/(?P<slug>(\w+[a-z\-]+))', armor_details, name='armor_details'),
    url(r'^tools/details/(?P<slug>(\w+[a-z\-]+))', tool_details, name='tool_details'),
    url(r'^mounts/details/(?P<slug>(\w+[a-z\-]+))', mount_details, name='mount_details'),



    # Search Pages:
    url(r'^search/$', search_home, name='search_home'),

    # Company Information
    url(r'^about_us/$', about_us, name='contact'),
    url(r'^report_issue/$', report_issue, name='report'),

    # DRF configuration
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
