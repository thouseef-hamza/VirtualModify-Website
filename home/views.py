from django.shortcuts import render
from .models import Blog,Service,Feature,Testimonial,Client,Carousel,Career,Enquiry,ContactUS,ApplyJob
from django.shortcuts import get_object_or_404
from .forms import EnquiryForm,ContactForm,ApplyJobForm


# Create your views here.

def homePage(request):
    features=Feature.objects.all()
    services=Service.objects.all()
    blogs=Blog.objects.all().order_by("-id")[:3]
    testimonials=Testimonial.objects.all().order_by("-id")[:6]
    clients=Client.objects.all()
    carousels=Carousel.objects.all().order_by("-id")
    response_data={
        "features":features,
        "services":services,
        "blogs":blogs,
        "testimonials":testimonials,
        "clients":clients,
        # "carousels":carousels[:carousels[0].item_count if carousels[0] else 0]
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
    careers=Career.objects.all()
    return render(request,"careers/career_list.html",{"careers":careers})

def career_detail(request,id):
    career=get_object_or_404(Career.objects.prefetch_related("job_type"),id=id)
    return render(request,"careers/career_detail.html",{"career":career})

def contact_us(request):
    return render(request,"contact_us.html")

from django.http import JsonResponse
def enquiry(request):
    forms = EnquiryForm(request.POST)
    if not forms.is_valid():
        return JsonResponse({"errors": forms.errors, "success": False, "status": 400})
    Enquiry.objects.create(
        website=forms.cleaned_data.get("website"),
        email=forms.cleaned_data.get("email")
    )
    return JsonResponse(
        {
            "message": "Form Submitted Successfully",
            "success": True,
            "status": 201,
        }
    )

def contact_us_view(request):
    forms = ContactForm(request.POST)
    if not forms.is_valid():
        return JsonResponse({"errors": forms.errors, "success": False, "status": 400})
    ContactUS.objects.create(
        first_name=forms.cleaned_data.get("first_name", None),
        last_name=forms.cleaned_data.get("last_name", None),
        email=forms.cleaned_data.get("email",None),
        phone_number=forms.cleaned_data.get("phone_number", None),
        message=forms.cleaned_data.get("message", None),
    )
    return JsonResponse(
        {
            "message": "Form Submitted Successfully",
            "success": True,
            "status": 201,
        }
    )

def apply_job(request):
    forms=ApplyJobForm(request.POST,request.FILES)
    if not forms.is_valid():
        return JsonResponse({"errors": forms.errors, "success": False, "status": 400})
    ApplyJob.objects.create(
        first_name=forms.cleaned_data["first_name"],
        last_name=forms.cleaned_data["last_name"],
        email=forms.cleaned_data["email"],
        cover_letter=forms.cleaned_data["cover_letter"],
        resume=forms.cleaned_data["resume"]
    )
    return JsonResponse(
        {
            "message": "Form Submitted Successfully",
            "success": True,
            "status": 201,
        }
    )
    
