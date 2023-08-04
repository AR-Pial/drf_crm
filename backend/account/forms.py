from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import Group
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

    USER_TYPES = (
        ('', 'Select'),
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('agent', 'Agent'),
        ('member', 'Member'),
    )
    user_type = forms.ChoiceField(choices=USER_TYPES,required=True)
    email = forms.EmailField(label="Email", required=True)
    first_name = forms.CharField(label="First Name", required=True)
    last_name = forms.CharField(label="Last Name", required=True)
    phone = forms.CharField(label="Phone", required=False)
    department = forms.CharField(label="Department", required=True)
    designation = forms.CharField(label="Designation", required=False)
    employee_id = forms.CharField(label="Employee Id", required=False)
    
    class Meta:
        model = User
        fields = ['password1','password2','first_name','last_name','email','user_type','phone','department','designation','employee_id']

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Email", required=True)

    class Meta:
        model = User
        fields = ['username', 'password']
    
