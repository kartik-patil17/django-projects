from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('todo',views.todo,name='todo'),
    path('submit',views.submit,name='submit'),
    path('todo/<int:id>',views.delete,name='delete'),
    path('todo/<int:id>',views.edit,name='edit'),
]

