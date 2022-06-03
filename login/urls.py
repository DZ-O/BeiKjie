from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from login import views

router = DefaultRouter()
router.register('books',views.UserViewSet,basename='login')

urlpatterns = [

]
urlpatterns += router.urls