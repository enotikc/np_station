from django import template
from django.db.models import F, Q
from ..models import ChatDialog, ChatMessage
from cuser.middleware import CuserMiddleware

register = template.Library()


def get_unread_dialogs(user_id):
	return ChatDialog.objects.filter(
		user__id=user_id,
		last_updated__gte=F('view_time'),
		is_hidden=False
	)


def get_unread_dialogs_count(user_id):
	return get_unread_dialogs(user_id).count()


def get_unread_messages_count(user_id):
	unread_dialogs = get_unread_dialogs(user_id)
	count = 0
	for d in unread_dialogs:
		c = ChatMessage.objects.filter(
			(
				Q(user_from=user_id, user_to=d.interlocutor) |
				Q(user_to=user_id, user_from=d.interlocutor)
			),
			add_time__gte=d.view_time
		)
		count += c.count()
	return count


@register.simple_tag
def unread_dialogs():
	user = CuserMiddleware.get_user()
	if user.is_authenticated():
		d_count = get_unread_messages_count(user.id)
		if d_count > 0:
			return "+{}".format(d_count)
	return ""
