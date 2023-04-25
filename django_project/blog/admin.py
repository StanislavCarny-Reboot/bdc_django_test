from django.contrib import admin
from .models import Member, CenterAdmin, Center

admin.site.register(Center)
admin.site.register(Member)
admin.site.register(CenterAdmin)
