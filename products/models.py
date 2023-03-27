from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """ Category model """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Brand(models.Model):
    """ Brand model """
    name = models.CharField(max_length=254)
    friendly_brand_name = models.CharField(
        max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_brand_name


class Product(models.Model):
    """ Product model """
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    brand = models.ForeignKey(
        'Brand', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    color = models.ForeignKey(
        'self', related_name='variants', on_delete=models.CASCADE,
        blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Testimony(models.Model):
    """ Testitmony model """
    SCORE_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    item = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='testimony')
    review_score = models.IntegerField(choices=SCORE_CHOICES, default=0)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """ Adding helpers for a better readability and user experience """
        ordering = ['created_on']
        verbose_name_plural = 'Testimonies'

    @property
    def rate(self):
        return self.review_score/5*100

    def __str__(self):
        """ Display the testimony """
        return f"Testimony {self.body}"
