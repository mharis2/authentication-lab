from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ('user',)

# c584e003d638ca97061db38ddda41b1803a54816

# Register your models here.
