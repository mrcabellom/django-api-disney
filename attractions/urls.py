from django.conf.urls import url, include
from attractions import views as attractions_view
from rest_framework.urlpatterns import format_suffix_patterns


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^attractions/$', attractions_view.get_attractions),
    url(r'^attractions/aggregate/$', attractions_view.get_attractions_aggregate),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = format_suffix_patterns(urlpatterns)