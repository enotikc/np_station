from django.conf.urls import patterns, include, url
from django.conf import settings
#from django.conf.urls.defaults import *
from django.db import router
from np_server.views import *
from np_server.models import *
from tastypie.api import Api
from np_server.api.resources import DeviceResource
#from api_v_1.views import *
#from api_v_1.models import *
from django.conf.urls import url, patterns, include
from django.contrib.auth.models import User, Group
#from rest_framework import viewsets, routers
#from rest_framework.urlpatterns import format_suffix_patterns
#from snippets.views import *

#router = routers.DefaultRouter()
#router.register(r'users', UserViewSet)
#router.register(r'groups', GroupViewSet)
#v1_api = Api(api_name='v1')
#v1_api.register(DeviceResource())


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'np_station.views.home', name='home'),
    # url(r'^np_station/', include('np_station.foo.urls')),
	(r'^$', index),
	(r'^test_user/$', test_user),
	(r'^blog/$', blog),
	(r'^about/$', about),
	(r'^accounts/login/base/where_device_data/$', where_device_data),
	(r'^accounts/login/base/actions/$', actions_webuser),
	(r'^accounts/login/$',  login),
	(r'^accounts/logout/$', logout),
	(r'^registration_page/$', registration_page),
	(r'^registration/$', reg_set),
	(r'^accounts/login/$', main_module),
	(r'^accounts/login/API_v1/$', API_generation),
	(r'^accounts/login/mvd/', mvd_message),
	(r'^accounts/login/alltools/', all_tools),
	(r'^accounts/login/task_manager_output/', task_manager_output),
	(r'^accounts/login/task_manager_input_first/', task_manager_input_first),
	(r'^accounts/login/task_manager_input_second/', task_manager_input_second),
	(r'^accounts/login/task_manager_input_third/', task_manager_input_third),
	(r'^accounts/login/task_card/', task_card),
	(r'^accounts/login/artist_message/', artist_message, {}, 'artist_message'),
	(r'^accounts/login/message_list/$', message_list, {}, 'message_list'),
	(r'^accounts/login/message_list/dialog_remove/(?P<user_id>\d+)/$', dialog_remove, {}, 'dialog_remove'),
	(r'^accounts/login/customer_menu/', customer_menu),
	(r'^accounts/login/artist_menu/', artist_menu),
	(r'^accounts/login/message_chat/(?P<user_id>\d+)/$', message_chat, {}, 'message_chat'),
	(r'^accounts/login/monitoring/$', monitoring_go),
	(r'^accounts/login/admin_panel/$', admin_panel_go),
	(r'^accounts/login/device_adding/$', device_adding_go),
	(r'^accounts/login/api/$', api_go),
	(r'^add_device/$', add_device_),
	(r'^save_device/$', save_device_),
	(r'^update_device/$', update_device_),
	(r'^API_v1/$', actions_for_mclient),
	#(r'^weblog/', include('zinnia.urls')),
	#(r'^comments/', include('django.contrib.comments.urls')),
	#(r'^api/', include(v1_api.urls)),
	# url(r'^', include(router.urls)),
	# url(r'^snippets/$', SnippetList.as_view()),
	# url(r'^snippets/(?P<pk>[0-9]+)/$', SnippetDetail.as_view()),
	# url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	(r'^api_v_1_doc/$', api_documentation),
	#url(r'^api_v_1s/$', API_DeviceList.as_view()),
    #url(r'^api_v_1s/(?P<pk>[0-9]+)/$', API_DeviceDetail.as_view()),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
#urlpatterns = format_suffix_patterns(urlpatterns)