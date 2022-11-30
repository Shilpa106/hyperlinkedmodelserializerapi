from rest_framework import routers
from app import views

app_name = 'app'

router = routers.DefaultRouter()
router.register(r'post', views.PostViewSet, basename="post")  # NOQA
router.register(r'user', views.UserViewSet, basename="user")  # NOQA

urlpatterns = router.urls

