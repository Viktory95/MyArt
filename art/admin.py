from django.contrib import admin
from art.models import Arts, Comments_art

class ArtsInline(admin.StackedInline):
    model = Comments_art
    extra = 2

class ArtsAdmin(admin.ModelAdmin):
    fields = ['art_title', 'art_text', 'art_date', 'art_link']
    inlines = [ArtsInline]
    list_filter = ['art_date']

admin.site.register(Arts, ArtsAdmin)