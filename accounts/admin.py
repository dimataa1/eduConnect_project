from django.contrib import admin
from .models import AppUser, Profile
from .forms import CustomUserForm, CustomUserChangeForm


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    add_form = CustomUserForm
    form = CustomUserChangeForm
    model = AppUser

    list_display = ('email', 'username', 'role', 'is_approved', 'is_active', 'is_staff')
    list_filter = ('role', 'is_approved', 'is_active', 'is_staff')
    search_fields = ('email', 'username', 'role')
    ordering = ('email',)
    actions = ['approve_teachers']

    def approve_teachers(self, request, queryset):
        count = queryset.filter(role='teacher', is_approved=False).update(is_approved=True)
        self.message_user(request, f"{count} teacher accounts approved.")
    approve_teachers.short_description = "Approve selected teacher accounts"


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'age', 'grade', 'subject')
    list_filter = ('user__role', 'grade', 'subject')
    search_fields = ('first_name', 'last_name', 'user__email', 'grade', 'subject')
    ordering = ('user__email',)

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user')
