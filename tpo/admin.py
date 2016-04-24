from django.contrib import admin
from tpo.models import UserProfile,Resume

# Register your models here.
admin.autodiscover()
admin.site.register(UserProfile)
admin.site.register(Resume)