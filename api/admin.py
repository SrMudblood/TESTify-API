from django.contrib import admin
from .models import US_female_name, US_male_name, US_last_name

# Register your models here.
admin.site.register(US_female_name)
admin.site.register(US_male_name)
admin.site.register(US_last_name)