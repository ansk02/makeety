from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.
class Product(models.Model):
	product_name = models.CharField('Produit', max_length=200, unique=True)
	slug         = models.SlugField(max_length=200, unique=True)
	description  = models.TextField(max_length=200, blank=True)
	price        = models.FloatField('Prix', default=0.0)
	images       = models.ImageField(upload_to='photos/produits')
	stock        = models.IntegerField(default=0)
	is_available = models.BooleanField('Disponible', default=True)
	category     = models.ForeignKey(Category, on_delete=models.CASCADE)
	create_date  = models.DateTimeField('Date d\'ajout', auto_now_add=True)
	modified_date= models.DateTimeField('Dernière modification', auto_now=True)

	class Meta:
		verbose_name = 'Produit'
		verbose_name_plural = 'Produits'

	def get_url(self):
		return reverse('product_detail', args=[self.category.slug, self.slug])


	def __unicode__(self):
		return self.product_name

