from django.contrib import admin
from webapp.models import Movie, Seat, Hall, Show, Category, Ticket, Discount, Booking


class MovieAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'release_date']
    ordering = ['-release_date']
    search_fields = ['name', 'id']


def list_admin_with_pk(*fields):
    class PkListAdmin(admin.ModelAdmin):
        list_display = ['pk'] + list(fields)
    return PkListAdmin


admin.site.register(Movie, MovieAdmin)
admin.site.register(Category, list_admin_with_pk('name'))
admin.site.register(Hall, list_admin_with_pk('name'))
admin.site.register(Seat, list_admin_with_pk('hall', 'row', 'seat'))
admin.site.register(Show, list_admin_with_pk('movie', 'hall', 'start_time', 'finish_time'))
admin.site.register(Ticket, list_admin_with_pk('show', 'seat', 'discount'))
admin.site.register(Discount, list_admin_with_pk('name', 'discount', 'start_date', 'finish_date'))
admin.site.register(Booking, list_admin_with_pk('show', 'status'))



