from django.contrib import admin
from .models import School, Post, Tour


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'grade', 'author', 'created_at')
    list_filter = ('subject', 'grade', 'author', 'created_at')
    search_fields = ('title', 'author__username', 'subject', 'grade')
    ordering = ('-created_at',)
    actions = ['activate_posts', 'deactivate_posts']

    def activate_posts(self, request, queryset):
        count = queryset.filter(is_active=False).update(is_active=True)
        self.message_user(request, f"{count} posts activated.")

    activate_posts.short_description = "Activate selected posts"

    def deactivate_posts(self, request, queryset):
        count = queryset.filter(is_active=True).update(is_active=False)
        self.message_user(request, f"{count} posts deactivated.")

    deactivate_posts.short_description = "Deactivate selected posts"



@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'town', 'description', 'image')
    list_filter = ('town',)
    search_fields = ('name', 'town', 'description')
    ordering = ('name',)


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('name', 'school', 'location', 'date', 'teacher', 'image')
    list_filter = ('school', 'location', 'date')
    search_fields = ('name', 'school__name', 'location', 'description')
    ordering = ('date',)
    date_hierarchy = 'date'
