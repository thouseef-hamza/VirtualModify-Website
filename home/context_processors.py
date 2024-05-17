from .models import Service,Career,Blog

def service_exist(request):
    return {"service_exist":Service.objects.exists()}

def career_exist(request):
    return {"career_exist":Career.objects.exists()}

def blog_exist(request):
    return {"blog_exist":Blog.objects.exists()}