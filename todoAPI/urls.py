from django.urls import path
from todoAPI.views import todoItem,todoList
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('get/',todoList.as_view()),  # This is use for to get all element at once.
    path('create/',todoList.as_view()),  # This is for to create item.
    path('get/<int:pk>/',views.todoItem.as_view()),   #This is for to get element by usning ID.
    path('update/<int:pk>/',views.todoItem.as_view()), # this is use for to update item by using id 
    path('delete/<int:pk>/',views.todoItem.as_view())  # this is used for delete item individually
    
]

urlpatterns = format_suffix_patterns(urlpatterns)