from django.contrib import admin
from .models import Form


""" Changing the default of admin site. """
class FormAdmin(admin.ModelAdmin):
    list_display = ("firstName", "lastName", "email")
    search_fields = ("firstName", "lastName", "email")
    list_filter = ("date", "occupation")
    ordering = ("-firstName",)
    readonly_fields = ("occupation",)

admin.site.register(Form, FormAdmin)
