from django import template
from django.db.models import F
from ..models import ChatDialog
from cuser.middleware import CuserMiddleware

register = template.Library()


def get_unread_dialogs_count(user_id):
	return ChatDialog.objects.filter(
		user__id=user_id,
		last_updated__gte=F('view_time'),
		is_hidden=False
	).count()


@register.simple_tag
def unread_dialogs():
	user = CuserMiddleware.get_user()
	if user.is_authenticated():
		d_count = get_unread_dialogs_count(user.id)
		if d_count > 0:
			return "+{}".format(d_count)
	return ""
