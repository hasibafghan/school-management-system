from django import forms
from .models import Student, Parent


class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student 
        fields = "__all__"
        widgets = {
            'date_of_birth': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',  # uses HTML5 datetime picker
            }),
        }
        exclude = ['parent' , 'slug' ]  # Exclude slug as it is auto-generated


class AddParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = '__all__'
