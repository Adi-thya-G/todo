from django import forms
from .models import Todo_table
from django.utils import timezone
class todo_create_form(forms.ModelForm):
     class Meta:
         model=Todo_table
         fields=['title','description','category','deadline','is_completed','priority_level','alternative_refernce']
     deadline = forms.DateTimeField(
         widget=forms.TextInput(attrs={'type': 'datetime-local'}),
         required=True
    )
     def clean_deadline(self):
          deadline=self.cleaned_data.get("deadline")
          if deadline and deadline<timezone.now():
               raise forms.ValidationError("deadline cannot be past")
          return deadline