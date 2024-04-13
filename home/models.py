from django.db import models

# Create your models here.

class Carousel(models.Model):
    title=models.CharField(max_length=40)
    sub_title=models.CharField(max_length=60,null=True,blank=True)
    image=models.ImageField(upload_to="carousel/")

    def __str__(self) -> str:
        return self.title

class Service(models.Model):
    title=models.CharField(max_length=100)
    logo=models.ImageField(upload_to="services/logo")
    image=models.ImageField(upload_to="services/")
    description=models.TextField(null=True,blank=True)

    def __str__(self) -> str:
        return self.title
    

class Blog(models.Model):
    title=models.CharField(max_length=60)
    image=models.ImageField(upload_to="blogs/")
    description=models.TextField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
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
    
class Career(models.Model):
    title=models.CharField(max_length=100)
    position=models.CharField(max_length=50)
    location=models.CharField(max_length=30)
    description=models.TextField()
    qualification=models.CharField(max_length=60)
    salary=models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.title
    
class ContactUS(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField()
    phone_number=models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.full_name()
    
    def full_name(self):
        return self.first_name + " " + self.last_name
    
class Client(models.Model):
    company_name=models.CharField(max_length=40)
    logo=models.ImageField(upload_to="clients/logo")

    def __str__(self) -> str:
        return self.company_name
    
