from django import forms
from .models import ChatMessage
from cuser.middleware import CuserMiddleware


class ChatMessageForm(forms.ModelForm):
	class Meta:
		model = ChatMessage
		exclude = ['user_from']
		widgets = {'user_to': forms.HiddenInput()}

	def __init__(self, *args, **kwargs):
		super(ChatMessageForm, self).__init__(*args, **kwargs)
		user = CuserMiddleware.get_user()
		if user.is_authenticated():
			self.instance.user_from = user
