from django import forms
from .models import ChatMessage


class ChatMessageForm(forms.ModelForm):
	class Meta:
		model = ChatMessage
		exclude = ['user_from']
		widgets = {'user_to': forms.HiddenInput()}
