#accounts/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Class, AvailableHour
from .forms import CustomUserCreationForm, AvailableHourForm
from django.shortcuts import redirect, get_object_or_404


@method_decorator(login_required, name='dispatch')
class AvailableHourCreateView(CreateView):
    model = AvailableHour
    form_class = AvailableHourForm
    template_name = 'add_hours.html'
    success_url = reverse_lazy('home')  # Redirect after successful submission

    def form_valid(self, form):
        form.instance.user = self.request.user  # Assign the TA to the hour entry
        return super().form_valid(form)

@login_required
def delete_available_hour(request, hour_id):
    hour = get_object_or_404(AvailableHour, id=hour_id, user=request.user)
    hour.delete()
    return redirect('home')    

class CustomUserCreationForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=[('student', 'Student'), ('ta', 'Teaching Assistant')])
    tutoring_hours = forms.CharField(max_length=100, required=False)
    ta_classes = forms.ModelMultipleChoiceField(queryset=Class.objects.all(), required=False)

    class Meta:
        model = CustomUser
        fields = ("username", "email", "age", "pronouns", "user_type", "tutoring_hours", "ta_classes")

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        # Check if the user type is 'ta' and set is_staff to True
        if form.cleaned_data['user_type'] == 'ta':
            user = form.save(commit=False)
            user.is_staff = True  #OMFG be TRUUUUUU
            user.save()# So it turns out you should totally like, save user
        else:
            user = form.save()
        
        return super().form_valid(form)