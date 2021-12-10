from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import *

# User = get_user_model()

class UserRegisterForm(forms.ModelForm):
    aadhar_no = forms.CharField(max_length=16)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'gender', 'email', 'phone']

    def clean_email(self,):
        email = self.cleaned_data.get('email')
        is_user_exist = User.objects.filter(email__exact=email)
        if is_user_exist:
            raise forms.ValidationError('Email is already taken')
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_2 = cleaned_data.get('confirm_password')
        if password is not None and password != password_2:
            self.add_error('confirm_password', 'your password must match')
        return cleaned_data

    def save(self, commit = True):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        user = super().save(commit=False)
        user.set_password(raw_password=password)
        if commit:
            user.save()
        return user
class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone']

    def clean(self):
        '''
        Verify both passwords match.
        '''
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password is not None and password != confirm_password:
            self.add_error("password_2", "Your passwords must match")
        return cleaned_data

    def save(self, commit=True):
        # Save the provided password in hashed format
        cleaned_data = super().clean()
        user = super().save(commit=False)
        user.set_password(cleaned_data.get('password'))
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['email', 'password', 'is_active', 'is_admin']

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField( widget=forms.PasswordInput({
        'class': 'form-control',
        'id': 'passwordId'
    }))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        print('username from ------------>'+username)
        user = User.objects.filter(username__iexact=username)
        print(user)
        if user is not None:
            return username
        else:
            return None
