from django.conf.urls import url
from finance.views import get_value_date, table_page

urlpatterns = [
	url(r'^$', get_value_date),
	url(r'^charges/$', table_page),
]