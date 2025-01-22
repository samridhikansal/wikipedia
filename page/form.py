from django.db import models
from django import forms
from .models import Topics, Comments

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topics
        fields = ("heading", 'desc', 'author_name', "image")
        
class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=500)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields =("comments",)