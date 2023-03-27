from django.test import TestCase
from .models import Product


class TestModel(TestCase):

    def test_done_default_to_false(self):
        product = Product.objects.create(name="Test product",
                                         description="Product description",
                                         price=499.99)
        self.assertFalse(product.sku)
