from django.contrib import admin
from .models import HepepsTeam,BackgroundImages, Services,Blog
# Register your models here.

admin.site.register(HepepsTeam)
# admin.site.register(Regions)
# admin.site.register(Districts)
# admin.site.register(Country)
admin.site.register(BackgroundImages)
admin.site.register(Services)
admin.site.register(Blog)