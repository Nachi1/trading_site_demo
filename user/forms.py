from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class Login_Form(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']