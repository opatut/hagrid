
from django.contrib import admin

from .models import *

admin.site.register(StoreSettings)
admin.site.register(Product)
admin.site.register(Variation)
admin.site.register(SizeGroup)
admin.site.register(VariationAvailabilityEvent)

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['name', 'group']
    list_display_links = ['group']
    list_filter = ['group']

