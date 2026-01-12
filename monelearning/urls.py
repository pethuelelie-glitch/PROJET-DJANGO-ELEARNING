from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('courses/', views.courses, name='courses'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('team/', views.team, name='team'),
    path('404/', views.page_no_found, name='404'),
    path('confirmation/', views.confirmation, name='confirmation'),
]
