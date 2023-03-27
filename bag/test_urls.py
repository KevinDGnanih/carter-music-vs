from django.test import SimpleTestCase
from django.urls import reverse, resolve
from bag.views import view_bag, add_to_bag, adjust_bag, remove_from_bag


class TestCartUrls(SimpleTestCase):

    def test_bag_url(self):
        url = reverse('view_bag')
        self.assertEqual(resolve(url).func, view_bag)

    def test_add_url(self):
        url = reverse('add_to_bag', args=['some-item'])
        self.assertEqual(resolve(url).func, add_to_bag)

    def test_adjust_url(self):
        url = reverse('adjust_bag', args=['some-item'])
        self.assertEqual(resolve(url).func, adjust_bag)

    def test_remove_url(self):
        url = reverse('remove_from_bag', args=['some-item'])
        self.assertEqual(resolve(url).func, remove_from_bag)
