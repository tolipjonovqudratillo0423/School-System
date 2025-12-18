from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .serializer import StudentSerializer,SchoolSerializer,ClassSerializer

from .models import Student,School,Class    

# Create your views here.
class StudentView(viewsets.ViewSet):

    def list(self,request):
        model =  Student.objects.all()
        serializer = StudentSerializer(model,many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def retrieve(self,request,pk=None):
        model = get_object_or_404(Student,pk=pk)
        serializer = StudentSerializer(model)
        return Response(serializer.data)    

    def update(self,request,pk):
        model = get_object_or_404(Student,pk=pk)
        serializer = StudentSerializer(model,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def partial_update(self,request,pk):
        model = get_object_or_404(Student,pk=pk)
        serializer = StudentSerializer(model,data = request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def destroy(self,request,pk):
        model = get_object_or_404(Student,pk=pk)
        model.delete()
        return Response({'message':"MODEL DELETED"})

class ClassView(viewsets.ViewSet):

    def list(self,request):
        model =  Class.objects.all()
        serializer = ClassSerializer(model,many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def retrieve(self,request,pk=None):
        model = get_object_or_404(Class,pk=pk)
        serializer = ClassSerializer(model)
        return Response(serializer.data)
    
    def update(self,request,pk):
        model = get_object_or_404(Class,pk=pk)
        serializer = ClassSerializer(model,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def partial_update(self,request,pk):
        model = get_object_or_404(Class,pk=pk)
        serializer = ClassSerializer(model,data = request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self,request,pk):
        model = get_object_or_404(Class,pk=pk)
        model.delete()
        return Response({'message':"MODEL DELETED"})

class SchoolView(viewsets.ViewSet):

    def list(self,request):
        model =  School.objects.all()
        serializer = SchoolSerializer(model,many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def retrieve(self,request,pk=None):
        model = get_object_or_404(School,pk=pk)
        serializer = SchoolSerializer(model)
        return Response(serializer.data)
    
    def update(self,request,pk):
        model = get_object_or_404(School,pk=pk)
        serializer = SchoolSerializer(model,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def partial_update(self,request,pk):
        model = get_object_or_404(School,pk=pk)
        serializer = SchoolSerializer(model,data = request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def destroy(self,request,pk):
        model = get_object_or_404(School,pk=pk)
        model.delete()
        return Response({'message':"MODEL DELETED"})


