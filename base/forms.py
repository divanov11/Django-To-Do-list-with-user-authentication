from django import forms
from django.contrib.auth.forms import UserCreationForm

# Reordering Form and View


class PositionForm(forms.Form):
    position = forms.CharField()

# class RegisterPage(forms.Form):
#     password1 = forms.CharField(
#         label='password 1 label',
#         strip=False,
#         widget=forms.PasswordInput(),
#         help_text='HELP TEXT',
#     )
#     password2 = forms.CharField(
#         label='password 2 label',
#         widget=forms.PasswordInput(),
#         strip=False,
#         help_text='HELP TEXT',
#     )