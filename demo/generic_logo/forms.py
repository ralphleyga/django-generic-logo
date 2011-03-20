from django import forms

from models import Glogo

class GlogoForm(forms.ModelForm):
	
	class Meta:
		model = Glogo
		fields = ['image']
