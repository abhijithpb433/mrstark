from .import views
from django.urls import path
app_name='jaya'
urlpatterns = [
    path('abcd/',views.jayasurya,name='abcd'),
    path('jjj/',views.abhijith,name='jjj'),
    path('hhh/',views.jithu,name='hhh'),
    path('lll/',views.ajin,name='lll'),
    path('sign/',views.deva,name='sign'),
    path('log/',views.ajin,name='log'),
    path('logout/',views.vipin,name='sss'),
    path('register/',views.reg,name='rrr')
]