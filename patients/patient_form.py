from django import forms
from .models import patients_entry

class PatientEntry(forms.Form):
	 	name = forms.CharField(max_length=100)
	 	last_name = forms.CharField(max_length=100)
	 	
		