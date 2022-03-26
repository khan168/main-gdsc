#handles all url routing

from django.urls import path
from .import views

urlpatterns = [
    path('',views.getRoutes),
    path('notes/',views.getNotes),
    path('notes/create/',views.createNote),
    path('notes/<str:pk>/update/',views.updateNote),
    path('notes/<str:pk>/delete/',views.deleteNote),
    path('notes/<str:pk>/',views.getNote),
    path('profile/create/', views.createprofile),
    path('profiles/',views.getprofiles),
    path('profiles/<str:e>', views.getprofile)

    

    
]