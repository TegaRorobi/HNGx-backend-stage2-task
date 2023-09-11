
from rest_framework import viewsets
from .models import Person
from .serializers import PersonSerializer


class PersonsViewSet(viewsets.ModelViewSet):
	'''
	This class contains various actions i.e list, create, retrieve, update, destroy
	which correspond to the various requests methods i.e get, post, get, put/patch, delete
	respectively, and these actions can be bundled separately to different url patterns.
	'''
	serializer_class = PersonSerializer
	queryset = Person.objects.all()
	lookup_field = 'name'

