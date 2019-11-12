from django.conf.urls import url
from . import views
app_name = 'qrcodes'

urlpatterns = [
			url(r'^$', views.index, name='index'),
			url(r'^topics', views.topics, name='topics'),
			url(r'^qr_topic/$', views.qr_topic, name='qr_topic'),
			url(r'^output/$', views.output, name='output'),
			]