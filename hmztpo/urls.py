from django.conf.urls import include, url
from django.contrib import admin
from tpo import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'hmztpo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^$', views.home),
    url(r'^logout$', views.logout),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
]
