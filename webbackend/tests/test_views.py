import json
from django.test import TestCase
from django.urls import reverse
from webbackend.models import Items

# Create your tests here.


"""
API views test
"""


class ApiViewTest(TestCase):
    def setUp(self):
        for i in range(5):
            Items.objects.create(
                title="title" + str(i),
                description="des" + str(i),
                image="image" + str(i),
            )

    # test getitem view
    def test_getItem(self):
        pk = 1
        response = self.client.get(reverse("getitem", kwargs={"pk": 6}))
        self.assertEquals(response.status_code, 404)

        response = self.client.get(reverse("getitem", kwargs={"pk": 1}))
        self.assertEquals(response.status_code, 200)

        response = self.client.get(reverse("getitem", kwargs={"pk": 1}))
        self.assertEquals(Items.objects.get(id=1).title, "title0")

    # test additem view
    def test_addItem(self):
        response = self.client.post(
            reverse("additem"),
            {
                "title": "my title",
                "description": "my description",
                "image": "my image",
            },
            format="json",
        )
        self.assertEquals(Items.objects.get(id=6).title, "my title")

    # test updateitem view
    def test_updateitem(self):
        newitem = Items.objects.create(
            title="newtitle", description="newdescription", image="newimage"
        )
        # )
        response = self.client.put(
            reverse("updateitem", kwargs={"pk": 6}),
            json.dumps(
                {
                    "title": "updated title",
                    "description": "new description",
                    "image": "pixx.jpg",
                }
            ),
            content_type="application/json",
        )
        newitem.refresh_from_db()
        self.assertEquals(newitem.title, "updated title")
        self.assertEquals(newitem.description, "new description")
        self.assertEquals(response.status_code, 200)

    # test deleteitem view
    def test_deleteitem(self):
        response = self.client.delete(reverse("deleteitem", kwargs={"pk": 1}))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(Items.objects.all().count(), 4)
