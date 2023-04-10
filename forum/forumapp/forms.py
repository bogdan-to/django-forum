from .models import Post
from django import forms


class NewPost(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['post_content']
        widgets ={
            'post_content': forms.Textarea(
                attrs={
                    'cols': 80, 
                    'rows': 3,
                    'class': 'form-control',
                    'wrap': 'soft',
                }
            )
        }