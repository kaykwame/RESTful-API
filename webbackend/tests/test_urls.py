from django.test import TestCase
from django.urls import reverse, resolve
from webbackend.views import (
    deleteitem,
    index,
    getitem,
    additem,
    updateitem,
    deleteitem,
    updatedb,
)

# Create your tests here.


"""
Testing API Urls
"""


class ApiUrlsTest(TestCase):
    def test_index_url_is_resolved(self):
        url = reverse("index")
        self.assertEquals(resolve(url).func, index)

    def test_updatedb_url_is_resolved(self):
        url = reverse("updatedb")
        self.assertEquals(resolve(url).func, updatedb)

    def test_additem_url_is_resolved(self):
        url = reverse("additem")
        self.assertEquals(resolve(url).func, additem)

    def test_getitem_url_is_resolved(self):
        url = reverse("getitem", args=["1"])
        self.assertEquals(resolve(url).func, getitem)

    def test_updateitem_url_is_resolved(self):
        url = reverse("updateitem", args=["1"])
        self.assertEquals(resolve(url).func, updateitem)

    def test_deleteitem_url_is_resolved(self):
        url = reverse("deleteitem", args=["1"])
        self.assertEquals(resolve(url).func, deleteitem)
