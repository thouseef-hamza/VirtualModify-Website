from django.shortcuts import render
from .models import Blog,Service,Feature,Testimonial,Client,Carousel
from django.shortcuts import get_object_or_404

# Create your views here.

def homePage(request):
    features=Feature.objects.all()
    services=Service.objects.all()
    blogs=Blog.objects.all().order_by("-id")[:3]
    testimonials=Testimonial.objects.all().order_by("-id")[:6]
    clients=Client.objects.all()
    carousels=Carousel.objects.all().order_by("-id")[:5]
    response_data={
        "features":features,
        "services":services,
        "blogs":blogs,
        "testimonials":testimonials,
        "clients":clients,
        "carousels":carousels
    }
    return render(request,"home/home.html",context=response_data)

def blog_list(request):
    blogs=Blog.objects.all()
    return render(request,"blog/blog_list.html",{"blogs":blogs})

def blog_detail(request,id):
    blog_detail=get_object_or_404(Blog,id=id)
    blogs=Blog.objects.exclude(id=id)
    response_data={
        "blog_detail":blog_detail,
        "blogs":blogs
    }
    return render(request,"blog/blog_detail.html",response_data)

def service_list(request):
    services=Service.objects.all()
    return render(request,"services/service_list.html",{"services":services})

def service_detail(request,id):
    service_detail=get_object_or_404(Service,id=id)
    services=Service.objects.exclude(id=id).values("id","title")
    response_data={
        "service_detail":service_detail,
        "services":services
    }
    return render(request,"services/service_detail.html",response_data)


def about_us(request):
    return render(request,"about_us.html")

def career_list(request):
    return render(request,"careers/career_list.html")

def career_detail(request,id):
    return render(request,"careers/career_detail.html")

def contact_us(request):
    return render(request,"contact_us.html")