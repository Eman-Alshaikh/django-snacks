from django.urls import path
from .views import (
     HomeView,
     aboutView
)

urlpatterns=[
    path('',HomeView.as_view(),name='home'),
    path('about',aboutView.as_view(),name='about'),


]