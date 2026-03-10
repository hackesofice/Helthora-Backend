from django.contrib import admin
from .models import Users, Doctors, DoctorsReviews, PatientsReviews, Messages

# Register your models here.
admin.site.register(Users)
admin.site.register(Doctors)
admin.site.register(DoctorsReviews)
admin.site.register(PatientsReviews)
admin.site.register(Messages)

