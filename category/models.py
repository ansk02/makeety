from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
	category_name = models.CharField('Categorie' , max_length=200, unique=True)
	slug = models.SlugField(max_length=200, unique=True)
	description =models.TextField(max_length=200, blank=True)
	image = models.ImageField(upload_to='photos/categories', blank=True)


	class Meta:
		verbose_name = 'Categorie'
		verbose_name_plural = 'Categories'

	def get_url(self):
		return reverse('products_by_category', args=[self.slug])


	def __str__(self):
		return self.category_name

