from .models import Person 
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
	'''
	serializer class to be used to convert python objects to json format on read operations e.g GET
	and from json formats to python objects on write operations e.g POST, PUT, PATCH.
	'''
	class Meta:
		model = Person 
		fields = '__all__'