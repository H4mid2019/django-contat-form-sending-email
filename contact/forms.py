from django import forms
from .models import Contact


class ContactReciver(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'comment', 'user_info')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'feedback-input'
        self.fields['name'].widget.attrs['placeholder'] = 'Name'
        self.fields['name'].widget.attrs['id'] = 'name'
        self.fields['email'].widget.attrs['class'] = 'feedback-input'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].widget.attrs['id'] = 'email'
        self.fields['comment'].widget.attrs['class'] = 'feedback-input'
        self.fields['comment'].widget.attrs['placeholder'] = 'Comment'
        self.fields['comment'].widget.attrs['id'] = 'comment'
