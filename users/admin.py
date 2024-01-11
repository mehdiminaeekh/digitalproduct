from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from .models import User, Province, UserProfile, Device


class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {
         'fields': ('first_name', 'last_name', 'phone_number', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff',
         'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'phone_number', 'password1', 'password2'),
        }),
    )

    list_display = ('username', 'phone_number', 'email', 'is_staff')
    search_fields = ('username__exact', )
    ordering = ('-id',)

    def get_search_results(self, request, queryset, search_term):
        queryset, my_have_duplicates = super().get_search_results(
            request, queryset, search_term,
        )

        try:
            search_term_as_int = int(search_term)
        except ValueError:
            pass
        else:
            queryset |= self.model.objects.filter(
                phone_number=search_term_as_int)
        return queryset, my_have_duplicates
    


class MyUserProfileAdmin(admin.ModelAdmin):
    fields = ['nick_name', 'birthday', 'gender', 'email', 'avatar', 'province']
    list_display = ['nick_name', 'birthday', 'gender', 'email']


class MyDeviceAdmin(admin.ModelAdmin):
    list_display = ('last_login', 'type_device')


admin.site.unregister(Group)
admin.site.register(Province)
admin.site.register(User, MyUserAdmin)
# admin.site.register(site)
admin.site.register(UserProfile, MyUserProfileAdmin)
admin.site.register(Device, MyDeviceAdmin)
