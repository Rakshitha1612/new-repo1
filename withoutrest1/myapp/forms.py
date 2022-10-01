from django import forms
from myapp.models import Student
class StudentForm(forms.ModelForm):
    def clean_marks(self):
        m=self.cleaned_data['marks']
        if m<35:
            raise Exception("Min marks must be 35 ")
        return m
    class Meta:
        model=Student
        fields="__all__"