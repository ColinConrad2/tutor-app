#pages.views
from accounts.models import CustomUser
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Filter users who are TAs (you could customize this if you have a 'role' field)
        ta_users = CustomUser.objects.filter(is_staff=True)  # Assuming TAs are marked as staff
        
        context['ta_users'] = ta_users  # Adding TA users to context
        return context


# Create your views here.
