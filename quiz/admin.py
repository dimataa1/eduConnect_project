from django.contrib import admin
from .models import Quiz, Question, Answer


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'text', 'question_type')
    list_filter = ('quiz', 'question_type')
    search_fields = ('text',)
    inlines = [AnswerInline]


class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'grade', 'created_at')
    search_fields = ('title', 'subject', 'grade')
    list_filter = ('subject', 'grade')
    ordering = ('-created_at',)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'text', 'is_correct')
    list_filter = ('is_correct',)
    search_fields = ('text',)
    list_editable = ('is_correct',)


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
