from django import forms
from django.forms import ModelForm
from .models import Question
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 
class QuestionForm(forms.Form):
    class Meta:
        model = Question
        fields = ('text')
 
#class addQuestionform(ModelForm):
    #class Meta:
        #model=QuesModel
        #fields="__all__"
