import re

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import UserProfile


def validate_phone_number(value):
    # Regular expression to match a typical phone number format
    phone_number_regex = r'^\+?1?\d{8,15}$'

    # Validate the phone number using the regular expression
    if not re.match(phone_number_regex, value):
        raise ValidationError(
            _('Enter a valid phone number.'),
            code='invalid_phone_number'
        )



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['age', 'comfortable_amount', 'expected_returns', 'risk_appetite', 'mobile']
    age = forms.IntegerField(label='Age', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your age'}))
    comfortable_amount = forms.IntegerField(label='Amount you need to live comfortably now?', widget=forms.NumberInput(attrs={'class': 'form-range', 'id': 'comfort-amount', 'min': 0, 'max': 20000, 'step': 100, 'value': 5000, 'class': 'form-control'}))
    expected_returns = forms.FloatField(label='Expected Returns (%)', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter expected returns'}))
    risk_appetite = forms.ChoiceField(label='Risk Appetite', choices=[
        ('', 'Select Risk Appetite'),
        ('Low', 'Conservative'),
        ('Medium', 'Moderate'),
        ('High', 'Aggressive'),
    ], widget=forms.Select(attrs={'class': 'form-select'}))
    mobile = forms.CharField(max_length=20, required=False, label='Mobile', validators=[validate_phone_number], widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Get Personalised Support[OPTIONAL]'}))

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))