from django.urls import path
#from django.urls import re_path as url
from . import views  

app_name='toplevel'
 

urlpatterns = [
    path('prices/', views.prices, name='prices'), 
    path('order/', views.order, name='order'), 
    path('terms-service/', views.terms_service, name='terms_service'),
    path('return-policy/', views.terms_service, name='return_policy'),
    path('contact/', views.contact, name='contact'),
    path('about-us/', views.about_us, name='about_us'), 
    path('terms-services/', views.terms_use, name='terms_use'), 
    path('order/', views.order, name='order'),  
    path('guarantees/', views.guarantees, name='guarantees'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('freelance-writer-position/', views.writing_opp, name='writing_opp'),
    path('subjects/', views.subjects_page, name='subjects_page'), 
    path('resources/', views.resources, name='resources_page'), 
    path('services/', views.service_pages, name='service_page'),
    path('FAQ/', views.faq, name='faq'),
    ]
