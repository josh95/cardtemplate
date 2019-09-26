

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cardeditorclothing/<int:clothing_id>', views.cardEditorClothing, name='cardeditcloth'),
    path('cardeditorpersona/<int:persona_id>', views.cardEditorPerson, name='cardeditperson'),
    path('cardeditorclothing/', views.cardEditorClothing, name='cardeditcloth'),
    path('cardeditorpersona/', views.cardEditorPerson, name='cardeditperson'),
    path('cardMain/', views.cardMain, name='cardmain'),
    path('saveChanges/', views.saveChanges, name='saveschanges'),
    path('saveChangesClothing/', views.saveChangesClothing, name='saveschangesclothing'),
    
]

