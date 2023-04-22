# Python
from typing import Any

# Django
from django.shortcuts import render
from django.db.models import QuerySet
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http import (
    HttpRequest,
    HttpResponse,
    QueryDict,
)
from rest_framework import generics
from django.core.files.uploadedfile import InMemoryUploadedFile

# Local
from .models import (
    Furniture,
    Rooms,
)
from abstracts.mixins import HttpResponseMixin
from abstracts import utils
from .forms import (
    FurnitureForm,
)
from .serializers import FurnitureSerializer


class FurnitureView(generics.RetrieveAPIView):
    serializer_class = FurnitureSerializer
    model = Furniture
    queryset = Furniture.objects.all()


