from django.contrib import admin

# Register your models here.

from .models import Gig, GigTier, Category

admin.site.register(Gig)
admin.site.register(GigTier)
admin.site.register(Category)