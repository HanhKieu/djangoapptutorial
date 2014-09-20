from django.contrib import admin
from polls.models import  Question , Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3 #provide enough fields for 3 questions
    #this class lets us to input choice only after we make question.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    fields = ['pub_date', 'question_text']
    inlines = [ChoiceInline]


admin.site.register(Question,QuestionAdmin)

# Register your models here.
