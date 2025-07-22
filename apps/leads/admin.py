from django.contrib import admin

# Register your models here.
from apps.leads.models import Agent, Lead, User

admin.site.register(User)
admin.site.register(Agent)
admin.site.register(Lead)