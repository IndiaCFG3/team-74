from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import StudentSerializer, EntrySerializer
from .models import Student, Entry


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('name')
    serializer_class =StudentSerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all().order_by('date_posted')
    serializer_class =EntrySerializer
