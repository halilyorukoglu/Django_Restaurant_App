from django.contrib import admin
from .models import LezzET 
from .models import home
from .models import services


class LezzETAdmin(admin.ModelAdmin):
    list_display = ("title","is_active","is_home","slug",)
    list_editable = ("is_active","is_home",)
    search_fields = ("title","description",)
    readonly_fields = ("slug",)


admin.site.register(home)

admin.site.register(services)

