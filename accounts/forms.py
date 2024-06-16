from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "age",
        )  # new


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "age",
        )  # new


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "password",)  # new

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 18:
            raise ValidationError("You must be 18 years or older to log in.")
        return age

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise ValidationError(("This account is inactive."), code="inactive", )
        if user.username.startswith("b"):
            raise ValidationError(("Sorry, accounts starting with 's' aren't welcome here."), code="no_b_users", )