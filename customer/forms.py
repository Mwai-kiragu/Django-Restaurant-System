from django import forms

class LoginForm(forms.form):
    username = forms.Charfield(max_length=100, widget= forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))