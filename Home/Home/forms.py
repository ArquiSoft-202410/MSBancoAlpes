from django import forms

from Home.models import User

class userForm(forms.Form):
    class Meta:
        model = User
        fields = ['name', 'lastName', 'country', 'city', 'phone', 'email', 'address']