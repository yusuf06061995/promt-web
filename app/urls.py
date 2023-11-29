from django.urls import path
from . views import *


urlpatterns = [
    path('',index,name='home'),
    path('about',about,name='about'),
    path('queryform',query_form,name='queryform'),
    path('support',support,name='support'),
    path('testimonial',testimonial,name='testimonial'),
    path('team',team,name='team'),


]