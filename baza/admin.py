from django.contrib import admin

# Register your models here.

from .models import Detail

class DetailAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',) # список полей в виде ссылки для перехода к соответствующей записи
    # search_fields = ('name',) # поля по которым можно производить поиск
    # list_filter = ('cost_cover_all',) # фильтр в правом sidebar'е
    # prepopulated_fields = {"slug": ("detail_name",)}

admin.site.register(Detail, DetailAdmin)