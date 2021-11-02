from django.urls import path
from . import views

urlpatterns = [
    # API Routes
    path("", views.index, name="index"),
    path("updatedb", views.updatedb, name="updatedb"),
    path("additem", views.additem, name="additem"),
    path("getitem/<int:pk>/", views.getitem, name="getitem"),
    path("updateitem/<int:pk>/", views.updateitem, name="updateitem"),
    path("deleteitem/<int:pk>/", views.deleteitem, name="deleteitem"),
]
