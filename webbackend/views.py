from django.shortcuts import render
from rest_framework import response

# from django.http import HttpResponse
# from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ItemsSerializer
from .models import Items
import json
from . import getdata
from django.shortcuts import get_object_or_404


# Create your views here.

# gets and displays all items in database
@api_view(["GET"])
def index(request):
    items = Items.objects.all()
    serializer = ItemsSerializer(items, many=True)
    return Response(serializer.data)


# get single JSON object from database
@api_view(["GET"])
def getitem(request, pk):
    item = get_object_or_404(Items, pk=pk)
    serializer = ItemsSerializer(item, many=False)
    return Response(serializer.data)


# add JSON object to database
@api_view(["POST"])
def additem(request):
    serializer = ItemsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


# update JSON object in database
@api_view(
    [
        "PUT",
    ]
)
def updateitem(request, pk):
    item = get_object_or_404(Items, pk=pk)
    # serializer = ItemsSerializer(instance=item, data=request.data)
    if request.method == "PUT":
        serializer = ItemsSerializer(instance=item, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# delete JSON object from database
@api_view(["DELETE"])
def deleteitem(request, pk):
    item = Items.objects.get(id=pk)
    item.delete()
    return Response("Item deleted successfully")


# pulls data from google spreadsheet, compares to existing data in database and saves ones that do not already exist in the database.
@api_view(["POST"])
def updatedb(request):
    # dbdata = Items.objects.all()
    mydata = getdata.values
    for x in mydata:
        try:
            print(x[0])
        except IndexError:
            x.insert(0, "")
        try:
            print(x[1])
        except IndexError:
            x.insert(1, "")
        try:
            print(x[2])
        except IndexError:
            x.insert(2, "")

        if Items.objects.filter(title=x[0], description=x[1], image=x[2]).exists():
            print("it exists")
        else:
            print("it does not exist")
            item = Items()
            item.title = x[0]
            item.description = x[1]
            item.image = x[2]
            item.save()
    return Response("DB update successful")
