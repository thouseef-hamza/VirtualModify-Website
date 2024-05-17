from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Carousel, Service, Blog, Testimonial, Feature, Career, ContactUS, Client, Enquiry, ApplyJob, JobType

@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
    search_fields = ('title',)
    list_filter = ('title',)

    class CarouselForm(forms.ModelForm):
        class Meta:
            model = Carousel
            fields = '__all__'

        def clean_title(self):
            title = self.cleaned_data.get('title')
            words = title.split()
            if len(words) < 1:
                raise ValidationError(
                    _('Title should not contain only one word.'),
                    code='invalid'
                )
            return title

    form = CarouselForm

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'logo',)
    search_fields = ('title',)
    list_filter = ('title',)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['logo'].help_text = "Copy-Paste Font Awesome Icon Code Snippet"
        form.base_fields['service'].required = False
        return form


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at',)
    search_fields = ('name',)
    list_filter = ('created_at',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('company_name',)
    search_fields = ('company_name',)

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description',)
    search_fields = ('title',)

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ('title', 'position', 'location',)
    search_fields = ('title', 'position',)
    list_filter = ('location', 'job_type',)

@admin.register(ContactUS)
class ContactUSAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number',)
    search_fields = ('first_name', 'last_name', 'email',)
    list_filter = ('email',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('company_name',)
    search_fields = ('company_name',)

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('website', 'email',)
    search_fields = ('email',)

@admin.register(ApplyJob)
class ApplyJobAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email',)
    search_fields = ('first_name', 'last_name', 'email',)
