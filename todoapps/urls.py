from django.urls import path
from . import views
urlpatterns =[
   path('create todo/',views.CreateTodoView.as_view())

]