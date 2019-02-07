"""Filtering and searching API in DRF https://www.django-rest-framework.org/api-guide/filtering/ """
from rest_framework import filters
from django.shortcuts import render
from rest_framework import generics
from filter_app.serializers import EmployeeSerializers
from filter_app.models import Employee
class EmployeeListAPI(generics.ListAPIView):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializers
	# filter_backends = (filters.SearchFilter,)
	# search_fields = ('eno', 'ename',)
	filter_backends = (filters.OrderingFilter,)
	ordering_fields = ('eno', 'ename')
	