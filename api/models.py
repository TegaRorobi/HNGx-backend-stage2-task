from django.db import models

# The resource we'll perform the CRUD operations on
class Person(models.Model):

	name = models.CharField(max_length=100, unique=True)
	email = models.EmailField()
	bio = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.name