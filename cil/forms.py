from django.forms import ModelForm
from .models import Profile


class GuestUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'exp', 'domain', 'designation', 'email', 'phone', 'biodata']
