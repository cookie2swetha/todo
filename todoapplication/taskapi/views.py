from django.shortcuts import render
from rest_framework.response import Response
from task.models import Todos
from taskapi.serializers import TodoSerializer
# Create your views here.
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.decorators import action

class TodoViewSetView(ViewSet):
    def list(self,request,*args,**kwargs):
        qs=Todos.objects.all()
        serializer=TodoSerializer(qs,many=True)#deserialize
        return Response(data=serializer.data)
    
    def create(self,request,*args,**kwargs):
        serializer=TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Todos.objects.get(id=id)
        serializer=TodoSerializer(data=request.data,instance=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    def retrive(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Todos.objects.get(id=id)
        serializer=TodoSerializer(qs)
        return Response(data=serializer.data)
    
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Todos.objects.filter(id=id).delete()
        return Response(data={"message":"todo deleted"})
    

class TodoViewSetView(ModelViewSet):
    serializer_class=TodoSerializer
    queryset=Todos.objects.all()

#localhost:8000/api/v1/todos/pending
#method : get
    @action(methods=["get"],detail=False)
    def pending(self,request,*args,**kwargs):
        qs=Todos.objects.filter(status=False)
        serializer=TodoSerializer(qs,many=True)
        return Response(data=serializer.data)
    
#localhost:8000/api/v1/todos/completed
#method : get    
    @action(methods=["get"],detail=False)
    def completed(self,request,*args,**kwargs):
        qs=Todos.objects.filter(status=True)
        serializer=TodoSerializer(qs,many=True)
        return Response(data=serializer.data)



    

        