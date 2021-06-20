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
	created_date  = models.DateTimeField('Date d\'ajout', auto_now_add=True)
	modified_date= models.DateTimeField('Dernière modification', auto_now=True)

	class Meta:
		verbose_name = 'Produit'
		verbose_name_plural = 'Produits'

	def get_url(self):
		return reverse('product_detail', args=[self.category.slug, self.slug])


	def __str__(self):
		return self.product_name



class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(variation_category='color', is_active=True)

    def sizes(self):
        return super(VariationManager, self).filter(variation_category='size', is_active=True)

variation_category_choice = (
    ('color', 'color'),
    ('size', 'size'),
)

class Variation(models.Model):
    product             = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category  = models.CharField('Couleur ou taille' ,max_length=100, choices=variation_category_choice)
    variation_value     = models.CharField('Valeur' ,max_length=100)
    is_active           = models.BooleanField('est-active' ,default=True)
    created_date        = models.DateTimeField('Date ajout' ,auto_now=True)

    objects = VariationManager()

    class Meta:
    	verbose_name = 'Variation'
    	verbose_name_plural = 'Variations'

    def __str__(self):
        return self.variation_value

