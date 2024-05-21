from django.urls import path
from .views import index
urlpatterns = [
    path("<str:roomname>/",index,name="home_page")
]
