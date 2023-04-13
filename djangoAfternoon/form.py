from django import forms
from djangoAfternoon.model import students


class EmpForm(forms.ModelForm):
    class Meta:
        model = students
        fields = "__all__"
