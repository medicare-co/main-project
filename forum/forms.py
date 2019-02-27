from django import forms
from forum.models import Question, Comment

class CreateQuestion(forms.ModelForm):

    class Meta:
        model = Question
        fields = (
            'question',
            'content',
        )

class PostComment(forms.ModelForm):

    class Meta:
        model = Comment
        fields = (
            'body',
        )