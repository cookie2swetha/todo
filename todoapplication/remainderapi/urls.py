from django.urls import path
from remainderapi import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()

router.register("todos",views.TodoViewSet,basename="todos")

urlpatterns=[

    path("register/",views.UserCreationView.as_view()),

    
]