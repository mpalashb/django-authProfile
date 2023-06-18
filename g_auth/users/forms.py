from typing import Any
from django import forms
from users.models import Profile


class ProfileForm(forms.ModelForm):
    bio = forms.CharField(max_length=225, widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = (
            "bio",
        )
