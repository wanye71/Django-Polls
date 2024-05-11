from django.contrib import admin

from .models import Question

# admin.site.register(Question)

class QuestionAdmin(admin.ModelAdmin):
    # fields = ["pub_date", "question_text"]
    fieldsets = [
        ("Questions", {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]})
    ]

admin.site.register(Question, QuestionAdmin)