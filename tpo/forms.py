from django import forms

from .models import UserProfile

class EditProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = '__all__'
        #exclude = ['user']
