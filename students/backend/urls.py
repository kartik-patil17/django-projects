from . import views
from django.urls import path

urlpatterns = [
    path('get/',views.get,name='get'),
    path('post/',views.post,name='post'),
    path('put/<int:id>',views.put,name='put'),
    path('delete/<int:id>',views.delete,name='delete'),
]
