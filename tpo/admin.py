from django.contrib import admin
from tpo.models import UserProfile

# Register your models here.
admin.autodiscover()
admin.site.register(UserProfile)