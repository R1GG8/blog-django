from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'status']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields.values():
    #         field.widget.attrs.update({'class': 'form-control'})