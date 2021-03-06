#
# Copyright (c) 2017 Red Hat, Inc.
#
# This software is licensed to you under the GNU General Public License,
# version 3 (GPLv3). There is NO WARRANTY for this software, express or
# implied, including the implied warranties of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. You should have received a copy of GPLv3
# along with this software; if not, see
# https://www.gnu.org/licenses/gpl-3.0.txt.
#
"""quipucords URL Configuration.

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
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),

    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include('api.urls')),

    url(r'^$', RedirectView.as_view(url='/login', permanent=False),
        name='home'),

    # ui routing
    url(r'^(?i)(client/(sources|scans|credentials|)(/|)(index.html|))$',
        TemplateView.as_view(template_name='client/index.html'),
        name='client'),

    # static files (*.css, *.js, *.jpg etc.)
    url(r'^(?!/?client/)(?P<path>.*\..*)$',
        RedirectView.as_view(url='/client/%(path)s', permanent=False),
        name='client'),
]
