from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status as STATUS
from rest_framework import decorators

from . import models
from . import serializers

# Create your views here.
@decorators.api_view(["GET"])
def status(request):

    total_users = models.Users.objects.count()

    # all_raw_doctors = models.Doctors.objects.all() ## returns an queryset
    # all_doctors = serializers.doctorSerializer(all_raw_doctors)
    # print(all_doctors)
    # total_doctors = len(all_doctors)
    total_doctors = models.Doctors.objects.count()

    data = {
        "totalDoctors": total_doctors,
        "totalUsers": total_users
    }

    return Response(data=data, status=STATUS.HTTP_200_OK)

@decorators.api_view(["GET"])
def users(request):
    all_raw_users = models.Users.objects.all() ## returns an queryset
    all_users = serializers.UsersSerializers(all_raw_users, many=True)
    return Response(data=all_users, status=STATUS.HTTP_200_OK)

@decorators.api_view(["GET"])
def user(request, email=None, user_id=None):
    """takes any of email and user_id and gives the user if found otherwise returns 404 with the message"""
    all_raw_users = models.Users.objects.all() ## returns an queryset
    all_users = serializers.UsersSerializers(all_raw_users, many=True)
    
    ## data if not found otherwise it will autometically overrriden by these conditional statements
    targeted_user = {"message": "Sorry, No user found with the provided information"}
    status = STATUS.HTTP_404_NOT_FOUND

    if user_id:
        targeted_user = all_users.filter(user_id=user_id)
        targeted_user["message"] = "User found"
        status = STATUS.HTTP_200_OK
        
    elif email:
        targeted_user = all_users.filter(email=email)
        targeted_user["message"] = "User found"
        status = STATUS.HTTP_200_OK

    res = Response(data=targeted_user, status=status)
    return res


    
