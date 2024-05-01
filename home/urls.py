from django.urls import path
from . import views

urlpatterns = [
    path("",views.homePage, name="home_page"),
    path("about_us/", views.about_us, name="about_us"),
    path("contact_us/", views.contact_us, name="contact_us"),
    path("blogs/",views.blog_list,name="blog_list"),
    path("blog/detail/<int:id>/",views.blog_detail,name="blog_detail"),
    path("services/",views.service_list,name="service_list"),
    path("service/detail/<int:id>/",views.service_detail,name="service_detail"),
    path("careers/",views.career_list,name="career_list"),
    path("career/detail/<int:id>/",views.career_detail,name="career_detail"),
    path("enquiry/",views.enquiry,name="enquiry"),
    path("contact/",views.contact_us_view,name="contact_us_view"),
    path("apply_job/",views.apply_job,name="apply_job")
]
