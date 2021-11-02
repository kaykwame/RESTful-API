from django.db import models

# Create your models here.


class Items(models.Model):

    """
    null, blank are true because the image column in the CSV dataset contains empty cells which will throw exceptions
    if the data is loaded into the SQLite db
    """

    title = models.CharField(max_length=50)
    description = models.TextField(default="", blank=True, max_length=500)
    image = models.CharField(default="", blank=True, max_length=100)

    def __str__(self):
        return self.title
