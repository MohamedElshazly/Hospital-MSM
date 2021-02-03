from django import forms
from django.contrib.auth.forms import UserCreationForm
from med.models import Department, Doctor, Engineer, Manager
from django_email_verification import send_email

class ManagerSignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Manager
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    
    def save(self):
        user = super().save(commit=False)
        user.type = 'MANAGER'
        user.is_active = False
        user.save()
        send_email(user)
        return user

class EngineerSignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Engineer
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

        # department = forms.ModelChoiceField(
        #     queryset=Department.objects.all().distinct(),
        #     widget=forms.Select
        # )
    
    def save(self):
        user = super().save(commit=False)
        user.type = 'ENGINEER'
        user.is_active = False
        user.save()
        send_email(user)
        return user

class DoctorSignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Doctor
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    
    def save(self):
        user = super().save(commit=False)
        user.type = 'DOCTOR'
        user.is_active = False
        user.save()
        send_email(user)
        return user
