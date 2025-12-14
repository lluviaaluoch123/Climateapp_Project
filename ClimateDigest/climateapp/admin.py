from django.contrib import admin

from . models import Contact,ClimateNews,ClimateTech,ClimateStory,Research

# Register your models here.
admin.site.register(Contact)
admin.site.register(ClimateNews)
admin.site.register(ClimateTech)
admin.site.register(ClimateStory)
admin.site.register(Research)


