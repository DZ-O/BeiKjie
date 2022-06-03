from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from feedbackApp import views

router = DefaultRouter()
# router.register('api/books',views.BookViewSet,basename='books')

urlpatterns = [

]
urlpatterns += router.urls