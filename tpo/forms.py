from django import forms
from django.forms import ModelForm, Textarea, DateInput
from functools import partial
from .models import UserProfile
from datetimewidget.widgets import DateTimeWidget


#DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class DateInput(forms.DateInput):
    input_type = 'date'

class EditProfileForm(forms.ModelForm):
    #date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))
    date_of_birth = forms.DateField(widget=DateInput())

    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'permanent_address': Textarea(attrs={'cols': 40, 'rows': 4}),
            'residential_address': Textarea(attrs={'cols': 40, 'rows': 4}),
            'date_of_birth': DateInput(),
            #'date_of_birth': DateTimeWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3)

        }
