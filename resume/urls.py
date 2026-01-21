from django.urls import path
from .import views

urlpatterns = [
    path('profile/', views.profile_create, name='profile_create'),
    path('education/', views.education_add, name='education_add'),
    path('project/', views.project_add, name='project_add'),
    path('preview/', views.resume_preview, name='resume_preview'),
    path('pdf/', views.resume_pdf, name='resume_pdf'),
    path('signup/', views.signup, name='signup'),
]
