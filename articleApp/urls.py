from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from articleApp import views

router = DefaultRouter()
router.register('article',views.ArticleViewSet,basename='文章')

urlpatterns = [

]
urlpatterns += router.urls