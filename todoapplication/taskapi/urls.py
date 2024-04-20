from django.urls import path
from taskapi import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()

router.register("v1/todos",views.TodoViewSetView,basename="todos")
router.register("v2/todos",views.TodoViewSetView,basename="todos")
# print(router.urls)

urlpatterns=[
    
    
]+router.urls