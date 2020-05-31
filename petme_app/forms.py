from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    class Meta:
        fields =("username", "email",
        "password", "address","phone")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label ="Email address"
        self.fields["address"].label = "Display address"
        self.fields["phone"].label ="Display phone"