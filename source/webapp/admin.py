from django.contrib import admin
from webapp.models import Movie
from webapp.models import Category


class MovieAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'release_date']
    ordering = ['-release_date']
    search_fields = ['name', 'id']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']
    ordering = ['name']
    search_fields = ['name', 'id']


admin.site.register(Movie, MovieAdmin)
admin.site.register(Category, CategoryAdmin)


