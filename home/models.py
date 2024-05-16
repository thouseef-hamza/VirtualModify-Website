from django.db import models
from django.core.exceptions import ValidationError
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
# Create your models here.

def validate_title(value):
    words = value.split()
    if len(words) < 1:
        raise ValidationError(
            _('Title should not contain only one word.'),
            code='invalid'
        )

class Carousel(models.Model):
    title=models.CharField(max_length=40,validators=[validate_title])
    description=models.TextField()
    image=models.ImageField(upload_to="carousel/images/",null=True,blank=True)

    @property
    def split_title(self):
        title_list = self.title.split(" ")
        main_title = " ".join(title_list[:-1])
        second_title = title_list[-1]
        return main_title, second_title
        


    def __str__(self) -> str:
        return self.title

class Service(models.Model):
    title=models.CharField(max_length=100)
    logo=models.CharField(max_length=100)
    image=models.ImageField(upload_to="services/")
    description=models.TextField(null=True,blank=True)

    def __str__(self) -> str:
        return self.title
    

class Blog(models.Model):
    name=models.CharField(max_length=60)
    sample_image=models.ImageField(upload_to="blog/",help_text="This is just for sample usage")
    created_at=models.DateTimeField(default=timezone.now)
    body=RichTextUploadingField(default='')

    def __str__(self) -> str:
        return self.name
    
class SubBlog(models.Model):
    title=models.CharField(max_length=60)
    mage=models.ImageField(upload_to="blogs/")
    description=models.TextField(null=True,blank=True)

    def __str__(self) -> str:
        return self.title
    

class Testimonial(models.Model):
    company_name=models.CharField(max_length=40)
    company_logo=models.ImageField(upload_to="testimonial/logo")
    company_person=models.CharField(max_length=25)
    description=models.TextField()

    def __str__(self) -> str:
        return self.company_name
    
class Feature(models.Model):
    title=models.CharField(max_length=150)
    short_description=models.CharField(max_length=150)
    logo=models.ImageField(upload_to="features/")

    def __str__(self) -> str:
        return self.title
    
class JobType(models.Model):
    name=models.CharField(max_length=125)
    
class Career(models.Model):
    title=models.CharField(max_length=100)
    position=models.CharField(max_length=50)
    location=models.CharField(max_length=30)
    description=models.TextField()
    qualification=models.CharField(max_length=60)
    salary=models.CharField(max_length=15)
    job_type=models.ManyToManyField(JobType,related_name="job_type")
    responsibilities=models.TextField()
    requirements=models.TextField()

    def __str__(self) -> str:
        return self.title
    
class ContactUS(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField(null=True)
    phone_number=models.CharField(max_length=15)
    message=models.TextField()

    def __str__(self) -> str:
        return self.full_name()
    
    def full_name(self):
        return self.first_name + " " + self.last_name
    
class Client(models.Model):
    company_name=models.CharField(max_length=40)
    logo=models.ImageField(upload_to="clients/logo/")

    def __str__(self) -> str:
        return self.company_name
    

class Enquiry(models.Model):
    website=models.URLField()
    email=models.EmailField()

    def __str__(self) -> str:
        return self.email
    
class ApplyJob(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    cover_letter=models.TextField()
    resume=models.FileField(upload_to="resume/")

    def __str__(self) -> str:
        return self.first_name