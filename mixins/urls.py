from django.urls import path
from .views import *
urlpatterns = [
    path('',my_view),
    path('get/',Studentlist.as_view()),
    path('create/',Studentcreate.as_view()),
    path('display/<int:pk>/',Studentdisplay.as_view()),
    path('update/<int:pk>/',Studentupdate.as_view()),
    path('delete/<int:pk>/',Studentdelete.as_view()),
    path('licre/',Studentlistcreate.as_view()),
    path('disupdel/<int:pk>',Studentdisupdel.as_view()),

]