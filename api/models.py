from django.db import models

# The resource we'll perform the CRUD operations on
class Person(models.Model):
	'''
	All fields contain only string datatypes, including
	the new primary key field 'name' instead of 'id'
	'''

	name = models.CharField(max_length=100, primary_key=True, unique=True)
	email = models.EmailField()
	bio = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.name