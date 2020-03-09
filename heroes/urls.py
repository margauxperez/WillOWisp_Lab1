#heroes/urls.py

from django.conf.urls import url
from .views import HomepageView, CloudView, SunfloweyView, JesterView

urlpatterns = [
	#url(r'^$', HomepageView.as_view(), name='homepage'),
	url(r'heroes/', HomepageView.as_view(), name='homepage'),
	url(r'/hero/cloud/', CloudView.as_view(), name='detail_cloud'),
	url(r'/hero/sunflowey/', SunfloweyView.as_view(), name='detail_sunflower'),
	url(r'/hero/jester/', JesterView.as_view(), name='detail_jester'),
]
