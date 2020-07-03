from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from django.contrib.admin.models import LogEntry

# Register your models here.
from .models import Books

class BooksAdmin(admin.ModelAdmin):
    list_display = ('isbn','title','author','genere','available')
    actions = ('mark_as_available', 'mark_as_unavailable', 'Stock_Sold')
    search_fields = ('isbn','title','author','genere')

    def mark_as_unavailable(self, request, queryset):
        count = queryset.update(available=False)
    
    def mark_as_available(self, request, queryset):
        count = queryset.update(available=True)
    
    def Stock_Sold(self, request, queryset):
            count = queryset.update(quantity = 0, available = False)


class MyAdminSite(AdminSite):
    pass

user_site = MyAdminSite(name='mysite')

user_site.register(Books, BooksAdmin)
admin.site.register(Books, BooksAdmin)


user_site.register(User)
user_site.register(Group)
admin.site.site_header = 'Library Management Portal'
admin.site.site_title = "Library"
admin.site.index_title = "Library"
user_site.site_header = 'Library Management Portal'
user_site.site_title = "Library"
user_site.index_title = "Library"
LogEntry.objects.all().delete()