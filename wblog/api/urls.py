from rest_framework import routers
from django.conf.urls import url
from django.urls import include, path
from .views import UserViewSet,PostDetailView,PostAPIView

from api import views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
# router.register(r'posts',PostView ,basename='posts')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url('login/',views.login),
    url(r'^posts-detail/(?P<pk>\d+)/$', PostDetailView.as_view(), name='posts'),
    url(r'^posts/', PostAPIView.as_view(), name='create-post'),
]