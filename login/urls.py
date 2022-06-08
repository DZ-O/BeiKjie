from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from login import views


urlpatterns = [
    # 注册
    path('api/phoneLogin/',views.UserRegisteredView.as_view()),


    # 登陆
    path("api/emailLogin/", views.LoginView.as_view({'post':'login'})),
]
router = DefaultRouter()
router.register('user',views.UserViewSet,basename='用户')
# router.register('user/login/',views.UserViewSet,basename='用户登录')
# router.register('user/registered/',views.UserRegisteredView,basename='用户注册')

urlpatterns += router.urls