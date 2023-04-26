from django.urls import path
from . views import index,registrations,update,delete

app_name = 'register'

urlpatterns = [
    path('',index,name='index'),
    path('registrations/',registrations,name='registrations'),
    path('registrations/<int:id>',registrations,name='registrations'),
    path('update/<int:id>/',update,name='update'),
    path('delete/<int:id>/',delete,name='delete'),
]
