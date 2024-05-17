from django.urls import path

from . import views


urlpatterns=[
    path('<int:pk>/',views.student_result, name='student_result'),
]