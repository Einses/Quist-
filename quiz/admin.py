from django.contrib import admin
from .models import Question, Choice

# Register your models here.
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text',)

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'ans1','ans2','ans3')

class Q_and_A(admin.AdminSite):
    site_header = 'Quist Admin area'

QA_site = Q_and_A(name='BlogAdmin')