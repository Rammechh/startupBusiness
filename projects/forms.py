from django.forms import ModelForm
from .models import Project, Review

from django import forms

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title','description','source_link','owner_name','featured_image', 'land_size','price', 'address', 'frontage', 'cmda_approved', 'direct_party']
        
    
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class' : 'input'})

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields =['value', 'body']
        labels = {
            'value' : "Place your vote",
            'body' : "Add a comment with your vote"
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class' : 'input'})