from django.urls import path
from . import views

urlpatterns = [
    path('',views.showrecord,name='showrecord'),
    path('register',views.register,name='register'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
]