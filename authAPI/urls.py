from django.urls import path
from .views import UserApiViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("login/",TokenObtainPairView.as_view()),
    path("register/",UserApiViewSet.as_view({"post": "create"})),

]
