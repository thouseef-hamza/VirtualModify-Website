from django.urls import path
from . import views

app_name="home"
urlpatterns = [
    path("",views.homePage,name="home_page")
]
