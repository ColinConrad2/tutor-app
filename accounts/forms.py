# accounts/forms.py
from .models import AvailableHour
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Class

class CustomUserCreationForm(UserCreationForm):
    USER_TYPE_CHOICES = [
        ('student', 'Student'),
        ('ta', 'Teaching Assistant'),
    ]

    # User type selection ( Student TA etc.)
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, label="User Type")
    
    # tutoring hours
    #tutoring_hours = forms.CharField(max_length=100, required=False, label="Tutoring Hours")
    
    # classes taught by TAs
    ta_classes = forms.ModelMultipleChoiceField(
        queryset=Class.objects.all(), 
        required=False, 
        label="Classes Teaching",
        widget=forms.CheckboxSelectMultiple()
    )

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "age",
            "pronouns",
            "user_type",     # NEW
            #"tutoring_hours", # NEW
            "ta_classes",     # NEW
        )

    # custom validation for TA users
    def clean(self):
        cleaned_data = super().clean()
        user_type = cleaned_data.get("user_type")
        ta_classes = cleaned_data.get("ta_classes")

        # Ensure that TAs select at least one class
        if user_type == 'ta' and not ta_classes:
            self.add_error('ta_classes', "Please select at least one class if you are a TA.")

        return cleaned_data
#form to handle time sceduling
class AvailableHourForm(forms.ModelForm):
    class Meta:
        model = AvailableHour
        fields = ['day_of_week', 'time_slot']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "age",
            "pronouns",
            #"tutoring_hours", 
            "ta_classes",     
        )