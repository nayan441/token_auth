
from multiprocessing import AuthenticationError
import re
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (UserSerializer, OrgSerializer, ChannelSerializer)
from .models import (User, Org, Channel)
from rest_framework import exceptions
# Create your views here.
from .authentication import create_access_token, create_refresh_token

class RegisterApiView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data

        if data['password'] != data['password_confirm']:
            raise exceptions.APIException("Password do not match")

        serializer = UserSerializer(data=data,)
        serializer.is_valid(raise_exception = True)
        
        serializer.save()
        return Response(serializer.data)

class LoginApiView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data["email"]
        password = request.data["password"]

        user = User.objects.filter(email=email).first()
        if user is None:
            raise  exceptions.AuthenticationFailed('Invalid Cred')
        if user.check_password(password):
            raise exceptions.APIException("Incorrect Password ")

        access = create_access_token(user.id)
        refresh = create_refresh_token(user.id)
        response = Response()
        response.data ={
            "token":access,
            "refresh":refresh
        }
        # serializer = UserSerializer(user)
        return response
