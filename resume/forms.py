from django import forms
from .models import Profile, Education, Project

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'bio', 'skills']
        widgets = {
            'bio': forms.Textarea(attrs={'rows':3}),
            'skills': forms.Textarea(attrs={'rows':2, 'placeholder': 'Python, Django, HTML'}),
        }

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['college', 'degree', 'year']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'tech_stack']
        widgets = {
            'description': forms.Textarea(attrs={'rows':3})
        }