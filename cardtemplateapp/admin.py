from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Personality
from .models import Clothing
admin.site.register(Clothing)
admin.site.register(Personality)
