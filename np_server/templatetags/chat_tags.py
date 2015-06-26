from django import template
from django.db.models import F
from ..models import ChatDialog
from cuser.middleware import CuserMiddleware

register = template.Library()


def get_unread_dialogs_count(user):
	return ChatDialog.objects.filter(
		user=user,
		last_updated__gte=F('view_time'),
		is_hidden=False
	).count()


@register.simple_tag
def unread_dialogs():
	d_count = get_unread_dialogs_count(CuserMiddleware.get_user())
	if d_count > 0:
		return "+{}".format(d_count)
	else:
		return ""
