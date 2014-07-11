from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from models import *


class RaceUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")

    def clean_username(self):
            # Since User.username is unique, this check is redundant,
            # but it sets a nicer error message than the ORM. See #13147.
            username = self.cleaned_data["username"]
            try:
                User.objects.get(username=username)
            except User.DoesNotExist:
                return username
            raise forms.ValidationError(
                self.error_messages['duplicate_username'],
                code='duplicate_username',
            )


class ClubForm(ModelForm):
    class Meta:
        model = Club

class RaceForm(ModelForm):
    class Meta:
        model = Race
        widgets = {
          'description': forms.Textarea(attrs={'rows':4}),
        }

class RacerForm(ModelForm):
    class Meta:
        model = Racer
        # self.fields['club'].queryset =
        # widgets = {
        #   'club': forms.ModelChoiceField()
        # }

class ResultForm(ModelForm):
    class Meta:
        model = Result

