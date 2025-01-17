#accounts/urls.py

from django.urls import path
from . import views
from .views import SignUpView, AvailableHourCreateView, delete_available_hour

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('add-hours/', AvailableHourCreateView.as_view(), name='add_hours'),
    path('delete-hour/<int:hour_id>/', delete_available_hour, name='delete_available_hour'),
    path('ta/<int:pk>/', views.ta_profile, name='ta_profile'),
]

