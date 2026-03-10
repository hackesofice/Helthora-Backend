from django.urls import path

from . import views as apiViews

urlpatterns = [
    path("", apiViews.status),
    path("users/", apiViews.users)
]