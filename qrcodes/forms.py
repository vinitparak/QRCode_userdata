from django import forms
from .models import qrcod


class QRForm(forms.ModelForm):
	class Meta:
		model = qrcod
		fields = ['text']
		labels = {'text':''}