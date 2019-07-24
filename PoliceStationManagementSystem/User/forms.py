from django.forms import ModelForm

from User.models import CrimeRecord


class MyModelForm(ModelForm):
    class Meta:
        model = CrimeRecord
        fields = ['Sex','EyeColor']