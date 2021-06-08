from django.urls import include, path
from rest_framework import routers
from bikeApp.views import UserViewSet, GroupViewSet
router = routers.DefaultRouter()
router.register(r"users",UserViewSet, basename="user")
router.register(r"groups",GroupViewSet)
urlpatterns =[
    path("api/", include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

