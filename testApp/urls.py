from django.urls import path
from testApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/',views.create_student, name='create'),
    path('update/<int:pk>/',views.update_student,name='update'),
    path('delete/<int:pk>/',views.delete_student,name='update'),
]