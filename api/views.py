
from rest_framework import viewsets
from .models import Person
from .serializers import PersonSerializer
from django.shortcuts import get_object_or_404

class IdOrNameLookupMixin:
	def get_object(self):
		"""
		Returns the object the view is displaying.

		You may want to override this if you need to provide non-standard
		queryset lookups.  Eg if objects are referenced using multiple
		keyword arguments in the url conf.
		"""
		queryset = self.filter_queryset(self.get_queryset())

		# Perform the lookup filtering.
		lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

		assert lookup_url_kwarg in self.kwargs, (
			'Expected view %s to be called with a URL keyword argument '
			'named "%s". Fix your URL conf, or set the `.lookup_field` '
			'attribute on the view correctly.' %
			(self.__class__.__name__, lookup_url_kwarg)
		)

		######## Customizations ###########
		arg = self.kwargs[lookup_url_kwarg]
		try:
			_ = int(arg)
			lookup_field = 'id'
		except:
			lookup_field = 'name'

		filter_kwargs = {lookup_field: self.kwargs[lookup_url_kwarg]}
		###################################

		obj = get_object_or_404(queryset, **filter_kwargs)

		# May raise a permission denied
		self.check_object_permissions(self.request, obj)

		return obj


class PersonsViewSet(IdOrNameLookupMixin, viewsets.ModelViewSet):
	'''
	This viewset contains various actions i.e list, create, retrieve, update, destroy
	which correspond to the various requests methods i.e get, post, get, put/patch, delete
	respectively, and these actions can be bundled separately to different url patterns.
	'''
	serializer_class = PersonSerializer
	queryset = Person.objects.all()
	lookup_url_kwarg = 'user_id'

	
