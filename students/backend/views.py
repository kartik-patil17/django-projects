from django.shortcuts import redirect, render
from .models import students
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import studentserializer

# Create your views here.

@api_view(['GET'])
def get(request):
    model = students.objects.all()
    serializer = studentserializer(model,many=True)

    return Response(serializer.data)

@api_view(['POST'])
def post(request):
    # model = students.objects.all()
    serializer = studentserializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def put(request,id):
    model = students.objects.get(pk=id)
    serializer = studentserializer(instance=model,data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def delete(request,id):
    model = students.objects.get(pk=id)
    model.delete()
    return redirect('get')