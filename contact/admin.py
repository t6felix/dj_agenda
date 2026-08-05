from django.contrib import admin
from contact import models

@admin.register(models.Contact)
# Register your models here.
class ContactAdmin(admin.ModelAdmin):


    list_display = 'id', 'first_name', 'last_name', 'phone', 'show',     # criar colunas na lista de contatos

    #demais configs
    ordering = 'id',
    list_filter = 'created_date',
    search_fields = 'first_name',
    list_per_page = 3
    list_max_show_all = 10
    list_editable = 'first_name', 'last_name', 'show'
    list_display_links = 'id', 'phone',


@admin.register(models.Category)
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = 'id',