from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


# for custom user signup form
class SignUpForms(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email': 'Email'}


class NewProfile(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login']
        labels = {'email': 'Email'}


class AdminProfile(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = '__all__'
        labels = {'email': 'Email'}
