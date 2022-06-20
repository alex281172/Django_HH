from django.contrib.auth.forms import UserCreationForm
from .models import ParsUser

class RegForm(UserCreationForm):
    class Meta:
        model = ParsUser
        fields = ('username', 'password1', 'password2', 'email')



