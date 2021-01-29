"""pharmacy URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from authentication import views as peekstudy_auth_views
from core import views as core_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from search import views as search_views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', core_views.home, name='home'),
    path('help/', core_views.help, name='help'),
    path('about/', core_views.about, name='about'),

    # auth urls
    path('login/', auth_views.LoginView.as_view(template_name='core/cover.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('signup/', peekstudy_auth_views.signup, name='signup'),
    path('signupdetailed/', peekstudy_auth_views.signupdetailed, name='signupdetailed'),

    # account urls
    path('settings/', core_views.settings, name='settings'),
    path('settings/picture/', core_views.picture, name='picture'),
    path('settings/upload_picture', core_views.upload_picture, name='upload_picture'),
    path('settings/save_uploaded_picture/', core_views.save_uploaded_picture, name='save_uploaded_picture'),
    path('settings/password/', core_views.password, name='password'),

    # admin url
    path('useradmin/', include('useradmin.urls')),

    # company url
    path('usercompany/', include('usercompany.urls')),

    # shop url
    path('usershop/', include('usershop.urls')),
    path('activities/', include('activities.urls')),
    path('search/', search_views.search, name='search'),
    path('user/<slug:username>', core_views.profile, name='profile')

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
