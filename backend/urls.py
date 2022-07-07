from backend.views import UserViewSet
from rest_framework.routers import DefaultRouter
from backend import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
urlpatterns= router.urls