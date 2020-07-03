from django import forms
from students.models import RegistrationForm

class Registration(forms.ModelForm):
    class Meta:
        model = RegistrationForm
        fields = "__all__"