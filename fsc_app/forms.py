from django import forms
from .models import  Project, DailyReport

class DailyReportModelForm(forms.ModelForm):
    class Meta:
        model = DailyReport
        fields = '__all__'

class ProjectModelForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'