from django.conf.urls import patterns, include, url
from django.conf import settings
from spectrablog.views import PostListView

urlpatterns = patterns('',
	url(r'^$', PostListView.as_view(), name='list'),
    url(r'^post/', include('spectrablog.urls'))
)


