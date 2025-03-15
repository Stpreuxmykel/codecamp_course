

from django.urls import path
from . import views


urlpatterns = [
    path('', views.sheir, name='hello_world'),
    path('meet/', views.contact, name='contact'),
    path('ajouter_etudiant/', views.student_create, name="add_student"),
    path("supprimer_etudiant/<int:id>/", views.delete_student,  name="delete_student"),
    path("update_student/<int:id>/", views.update_student, name="edit_student")
]
