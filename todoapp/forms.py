from django import forms
from django.forms import ModelForm
from .models import *

class TaskForm(forms.ModelForm):
	title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Task...'}), label=False)
	complete_time = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Completation date...'}), label=False)

	class Meta:
		model = Task
		fields = '__all__'

class UpdateTaskForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Task ...'}), label=False)


	class Meta:
		model = Task
		fields = '__all__'

