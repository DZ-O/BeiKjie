from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from login import views
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    # 注册
    path('phoneLogin/',views.UserRegisteredView.as_view()),

    # 登陆
    path("emailLogin/", views.LoginView.as_view({'post':'login'})),
    path("docs/", include_docs_urls(title='用户api')),
]
router = DefaultRouter()
router.register('user',views.UserViewSet,basename='用户')
router.register('icon',views.UserIconView,basename='icon')
# router.register('user/registered/',views.UserRegisteredView,basename='用户注册')

urlpatterns += router.urls