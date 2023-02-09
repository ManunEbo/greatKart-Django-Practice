from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


# Register your models here.

class AccountAdmin(UserAdmin):
    # specify the fields to be displayed in the admin panel
    list_display = ('email', 'firstname', 'lastname', 'username','last_login', 'date_joined','is_active')

    # applying links that will open the details page on field names
    list_display_links = ('email', 'firstname', 'lastname')

    # Specifying readonly fields
    readonly_fields = ('last_login', 'date_joined') 

    # order users by date joined in descending order ('-date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
