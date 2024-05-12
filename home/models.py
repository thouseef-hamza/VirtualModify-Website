from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Carousel(models.Model):
    title=models.CharField(max_length=40)
    sub_title=models.CharField(max_length=60,null=True,blank=True)
    image=models.ImageField(upload_to="carousel/images/",null=True,blank=True)
    video=models.FileField(upload_to="carousel/videos/",null=True,blank=True)
    item_count=models.IntegerField(default=5)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        # If it's a new object or item_count is changed
        if not self.pk or self._state.adding or 'item_count' in self.get_dirty_fields():
            first_carousel = Carousel.objects.first()
            if first_carousel:
                self.item_count = first_carousel.item_count
        super().save(*args, **kwargs)

class Service(models.Model):
    title=models.CharField(max_length=100)
    logo=models.ImageField(upload_to="services/logo")
    image=models.ImageField(upload_to="services/")
    description=models.TextField(null=True,blank=True)

    def __str__(self) -> str:
        return self.title
    

class Blog(models.Model):
    name=models.CharField(max_length=60)
    sample_image=models.ImageField(upload_to="blog/",help_text="This is just for sample usage")
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