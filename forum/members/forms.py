from .models import Member
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.core.exceptions import ValidationError

class MemberCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = 'Lozinka *'
        self.fields['password1'].help_text = None
        self.fields['password2'].label = 'Ponovljena lozinka *'
        self.fields['password2'].help_text = None
        self.fields['email'].required = True
        for visible in self.visible_fields():
            visible.field.widget.attrs.update({'class': 'form-control'})


    class Meta:
        model = Member
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']
        labels ={
            'first_name': 'Ime',
            'last_name': 'Prezime',
            'username': 'Korisničko ime *',
            'email': 'Mejl *',
        }

        help_texts ={
            'username': None,
        }


class MemberAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs.update({'class': 'form-control'})


class MemberChangeForm(UserChangeForm):

    class Meta:
        model = Member
        fields = ['first_name', 'last_name','username', 'email']
        labels ={
            'first_name': 'Ime',
            'last_name': 'Prezime',
            'username': 'Korisničko ime *',
            'email': 'Mejl *',
        }

        help_texts ={
            'username': None,
        }

